from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.utils.mongo import mongo_instance
from app.utils.core import get_user_id

#叶子节点的blueprint不加url_prefix
recent_router = APIRouter()

@recent_router.post('/recent')
async def operator(
    pageSize: int = Body(20),
    pageNum: int = Body(0),
    figureName: str = Body(""),
):
    # 获取当前用户ID
    user_id = get_user_id()
    
    # 计算跳过的文档数量
    skip = pageSize * pageNum
    
    # 查询条件
    query = {
        "user_id": user_id,
        "status": "active"
    }
    
    # 如果figureName不为空，添加角色名称的模糊查询条件
    if figureName:
        query["role_name"] = {"$regex": figureName, "$options": "i"}  # i表示不区分大小写
    
    # 获取总记录数
    total = await mongo_instance.count(
        "roles", 
        query
    )
    
    # 计算总页数
    total_pages = (total + pageSize - 1) // pageSize if total > 0 else 0
    
    # 查询角色数据，按照最后更新时间倒序排序
    roles = await mongo_instance.find_many(
        "roles",
        query,
        skip=skip,
        limit=pageSize,
        sort=[("last_updated_at", -1)]
    )
    
    # 构建返回的记录列表
    records = []
    
    # 收集所有需要查询的资源ID
    resource_ids = [role.get("selected_role_resource_id") for role in roles if role.get("selected_role_resource_id")]
    
    # 批量查询资源
    resources = {}
    if resource_ids:
        resource_list = await mongo_instance.find_many(
            "role_resources",
            {
                "_id": {"$in": resource_ids},
                # "resource_url": {"$ne": ""}  # 确保resource_url不为空
            }
        )
        resources = {str(resource["_id"]): resource for resource in resource_list}
    
    # 构建返回数据
    for role in roles:
        selected_resource_id = role.get("selected_role_resource_id")
        if selected_resource_id:
            resource_id_str = str(selected_resource_id)
            if resource_id_str in resources:
                resource = resources[resource_id_str]
                records.append({
                    "id": str(role["_id"]),
                    "cnDesc": resource.get("description", ""),
                    "figureName": role.get("role_name", ""),
                    "url": resource.get("resource_url", ""),
                })
    
    return JSONResponse(content={
        "code": 0,
        "data": {
            "records": records,
            "total": total,
            "size": pageSize,
            "current": pageNum + 1,  # 前端从1开始计数
            "pages": total_pages,
        },
        "msg": "",
    })