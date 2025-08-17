from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id
from app.locales.translations import get_translation
import logging

delete_router = APIRouter()

@delete_router.post('/delete')
async def operator(
    projectId: str = Body(...),
    roleId: str = Body(...)
):
    user_id = get_user_id()
    project_id = mongo_instance.generate_object_id(projectId)
    role_id = mongo_instance.generate_object_id(roleId)

    # 校验项目是否存在
    project = await mongo_instance.find_one(
        "projects",
        {
            "_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    if not project:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("project_not_found"),
        })

    # 校验角色是否存在
    role = await mongo_instance.find_one(
        "roles",
        {
            "_id": role_id,
            "project_id": project_id,
            "user_id": user_id,
            "status": "active"
        }
    )
    if not role:
        return JSONResponse(content={
            "code": 1,
            "data": None,
            "msg": get_translation("role_not_exist_or_no_right"),
        })

    # 逻辑删除角色（只修改status）
    await mongo_instance.update_one(
        "roles",
        {
            "_id": role_id,
            "project_id": project_id,
            "user_id": user_id
        },
        {
            "$set": {"status": "inactive"}
        }
    )
    
    #需要从项目的分镜中删除角色ID
    role_id_str = str(role_id)
    
    # 查找项目中所有包含该角色的分镜
    shots = await mongo_instance.find_many(
        "shots",
        {
            "project_id": project_id,
            "user_id": user_id,
            "status": "active",
            "selected_roles.role_id": role_id
        }
    )
    
    update_count = 0
    current_time, _, _ = mongo_instance.get_current_time()
    
    # 遍历所有分镜，移除角色ID
    for shot in shots:
        shot_id = shot["_id"]
        
        # 1. 从selected_roles中移除角色
        selected_roles = shot.get("selected_roles", [])
        new_selected_roles = [role for role in selected_roles if str(role.get("role_id")) != role_id_str]
        
        # 2. 从dialogues中移除角色的台词
        dialogues = shot.get("dialogues", [])
        new_dialogues = [dialogue for dialogue in dialogues if dialogue.get("role_id") != role_id_str]
        
        # 更新分镜
        result = await mongo_instance.update_one(
            "shots",
            {"_id": shot_id},
            {
                "$set": {
                    "selected_roles": new_selected_roles,
                    "dialogues": new_dialogues,
                    "last_updated_at": current_time
                }
            }
        )
        
        if result.modified_count > 0:
            update_count += 1
            
    logging.info(f"已从项目 {project_id} 的 {update_count} 个分镜中移除角色 {role_id}")

    # 从项目中移除角色ID
    await mongo_instance.update_one(
        "projects",
        {"_id": project_id},
        {
            "$set": {"last_updated_at": current_time},
            "$pull": {"role_ids": role_id}
        }
    )

    return JSONResponse(content={
        "code": 0,
        "data": None,
        "msg": get_translation("delete_role_success")
    })