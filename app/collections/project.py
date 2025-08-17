"""项目的功能类，对应于mongo中的数据结构
#用户项目
projects = {
    "_id": ObjectID,
    "user_id": ObjectID,
    "status":"active", #删除后变为inactive
    "project_language": "zh-CN", #项目语言，一般以开始输入的脚本自身语言来判断。
    "project_name": "新建项目2025-01-17_23:38",
    "project_type": 0, #0 新建 1 模版复制 2 项目复制 4 某个url
    "image_model_name": "model name", #生图模型名称，对应月不同的API接口，和style_type 配合获取模型模版id，用于图片生成
    "style_type": 11, #style需要从模型API的接口获取
    "style_type_desc": "动漫2.0", #从风格配置表获取
    "picture_size": "3:2",#画面尺寸，可以进行换算成真实大小
    "image_size":"1344x768", #图片大小
    "cover": "https://static.chuangyi-keji.com/2025/01/26/assets/png/4d1da24b-9e34-4f0d-b8d0-fbec6a25c432.png?x-oss-process=image/resize,w_500,limit_0",
    "script_type": 1,# 0 模版生成 1 AI生成 2 用户输入（包括示例故事） 3 文件读取 4 空项目
    "script_content": "",#脚本内容
    "times_and_culture":"描述年代，文化元素，建筑风格、音乐风格、道具风格等", #用大模型从脚本中获取，在生成场景时使用
    "times_and_culture_en":"times_and_culture的英文描述", #用大模型从脚本中获取，在生成场景时使用
    "has_shot": True,
    "has_role": True,
    "has_storyboard": True,
    "generate_seed": 123456789, #生成种子,用户生成图片或者视频（100000-999999之间）
    "shot_ids":[ObjectID,ObjectID], #场景ID列表，顺序代表了显示顺序。0显示在上端，1 显示在0的下面 对应于 shots 集合,如果删除场景，这里要同步更新
    "role_ids":[ObjectID,ObjectID], #角色ID列表，顺序代表了显示顺序。0显示在上端，1 显示在0的下面 对应于 roles 集合，如果删除角色，这里要同步更新
    "voiceover_model_name": "model_name", #旁白的音效模型
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

#项目镜头
shots ={
    "_id": ObjectID,
    "user_id": ObjectID,
    "project_id":ObjectID,
    "status":"active", #删除后变为inactive
    "background":"描述空间环境、光照、天气",#画面描述，selected_roles 共同组合为 画面描述和出场人物
    "background_en":"background的英文描述", #英文背景描述
    "selected_roles":[{ "role_id":ObjectID, #对应于roles集合
                        "action_and_emotion":"XXXXX", #描述状态和情绪 比如 兴奋,四处张望，与ID同步修改
                        "action_and_emotion_en":"XXXXX", #英文描述状态和情绪 比如 兴奋,四处张望，与ID同步修改
                       }
                    ], #角色ID列表，顺序代表了显示顺序。0显示在上端，1 显示在0的下面
    #台词
    "dialogues":[{"role_id":"voiceover", "content":"XXXXX"}, #voiceover 代表旁白
               {"role_id":str(ObjectID), "content":"早上好"},#与ID同步修改
               {"role_id":str(ObjectID), "content":"你吃了吗？"},#与ID同步修改
               ], #台词，按照顺序显示和播放。由于monogodb的查询问题，需要考虑voiceover，所以这里 roleid的objectid转为字符串存储
    "selected_shot_resource_id":ObjectID, #当前选中镜头资源ID
    "shot_size":"景别，用数字0,1,2,3,4表示，0表示远景、1表示全景、2表示中景、3表示近景、4表示特写", 
    "camera_angle":"机位角度，用数字0,1,2,3,4表示，0表示视平、1表示仰角、2表示俯角、3表示鸟瞰、4表示倾斜角", 
    "shot_type":"摄影机运动，用数字0,1,2,3,4,5,6表示，0表示固定镜头、1表示推镜头、2表示拉镜头、3表示摇镜头、4表示移镜头、5表示俯仰镜头、6表示变焦镜头", 
    "shot_time":"1", #镜头时长 用数字表示，单位秒
    "shot_resource_ids":[ObjectID,ObjectID], #镜头资源列表。对应于shot_resources集合。 顺序代表了显示顺序。0显示在前面，1 显示在0的后面。比如 当前镜头的画面历史记录
    "other_info":[], #其他信息 用户可以写入备注信息
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

| # | 中文名称     | 英文术语             | 简要说明                | 关键词        | 常见用途            |
| - | -------- | ---------------- | ------------------- | ---------- | --------------- |
| 0 | **固定镜头** | Fixed Shot      | 相机完全不动，场面由被摄体移动     | 冷静、观察、构图   | 舞台感、冷眼旁观、构图张力   |
| 1 | **推镜头**  | Push In          | 相机向前推进靠近主体，强调情绪或细节  | 靠近、聚焦、压迫感  | 表现角色内心转变、情绪爆发   |
| 2 | **拉镜头**  | Pull Out         | 相机向后移动远离主体，拉远空间感    | 疏离、孤独、揭示环境 | 渐显场景全貌、突显孤立感    |
| 3 | **摇镜头**  | Pan (Left/Right) | 相机水平原地旋转，横向展示画面     | 转场、空间展示    | 场景切换、两人物对话、追视物体 |
| 4 | **俯仰镜头** | Tilt (Up/Down)   | 相机垂直原地旋转，上下观察空间     | 高度、权力、揭示   | 仰望建筑、俯瞰角色、主观视觉  |
| 5 | **移镜头**  | Dolly / Tracking | 相机整体平稳移动，通常用于跟拍     | 跟随、沉浸、连续   | 人物走动、场景穿梭、长镜头   |
| 6 | **变焦镜头** | Zoom In / Out    | 调节镜头焦距放大/缩小主体，不移动相机 | 压缩、冲击、聚焦   | 表现震惊、快速拉近、视角切换  |


#镜头资源表
shot_resources ={
    "_id": ObjectID,
    "user_id": ObjectID,
    "project_id":ObjectID,
    "shot_id":ObjectID,
    "image_model_name": "model name", #生图模型名称，对应月不同的API接口，和style_type 配合获取模型模版id，用于图片生成
    "style_type": 2, #对应于 data.styles[style_id]  风格
    "style_type_desc": "动漫2.0",
    "image_size": "1344x768", #画面尺寸
    "generate_seed": 123456789, #生成种子,用户生成图片或者视频（100000-999999之间）
    "generate_id": "", #生成ID
    "generate_status":"", #生成状态 done 或 processing
    "resource_type": 1, #0 空白 #1 图片 2 视频
    "resource_url": "https://chuangyi-keji.com/2025/01/26/assets/png/4d1da24b-9e34-4f0d-b8d0-fbec6a25c432.png?x-oss-process=image/resize,w_500,limit_0",
    "resource_prompt":"", #生成资源的模型提示语
    "is_HD": False, #是否高清 对原始尺寸放大一倍。
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

#项目角色
roles ={
    "_id": ObjectID,
    "user_id": ObjectID,
    "project_id":ObjectID,
    "status":"active", #删除后变为inactive
    "role_name": "角色1", #这个字段比较特殊。角色资源不应该有role_name字段，但是这个字段是可以修改的。比如10岁和20岁的角色两个角色。
    "selected_role_resource_id":ObjectID, #当前选中角色资源ID
    "role_resource_ids":[ObjectID,ObjectID], #历史记录,按照顺序显示。对应于role_resources集合
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

#角色资源表
role_resources ={
    "_id": ObjectID,
    "user_id": ObjectID,
    "project_id":ObjectID,
    "role_id":ObjectID,
    "description":"23岁的中国女性，身高 165cm，体重50kg。中等身材，红色卷发，长发，穿着休闲舒适的粉色长裙，色彩明亮柔和。", #角色描述
    "description_en":"23-year-old Chinese woman, medium build, red curly hair, long hair, wearing casual comfortable pink skirt, bright and soft colors.", #角色描述英文
    "image_model_name": "model name", #生图模型名称，对应月不同的API接口，和style_type 配合获取模型模版id，用于图片生成
    "style_type": 2, #对应于 data.styles[style_id]  风格
    "style_type_desc": "动漫2.0",
    "image_size": "576x1024", #画面尺寸。角色采用固定尺寸576x1024
    "generate_seed": 123456789, #生成种子,用户生成图片或者视频（100000-999999之间）
    "generate_id": "", #生成ID
    "generate_status":"", #生成状态 done 或 processing 或者 failed
    "resource_url": "https://uangyi-keji.com/2025/01/26/assets/png/4d1da24b-9e34-4f0d-b8d0-fbec6a25c432.png?x-oss-process=image/resize,w_500,limit_0",
    "resource_prompt":"", #生成资源的模型提示语
    "voice_model_name":"", #角色语音模型名称
    "face_image":"https://www.baidu.com", #参考人脸图
    "projection_image":["正面","背面","左面","右面"], #多面图
    "last_updated_at": datetime.now(),
    "created_at": datetime.now(),
    "created_at_str": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

"""
"""项目的功能类"""
import logging,os
from app.locales.translations import get_project_description_item,get_project_role_item,get_project_shot_item
from app.utils.mongo import mongo_instance
from datetime import datetime
import random  # 添加random模块导入
from app.models.model_factory import create_image_model


#从模版数据创建工程
async def copy_project_from_template(user_id, template_id):
    """
    根据模板ID复制一个新项目
    
    Args:
        user_id: 用户ID
        template_id: 模板ID
    
    Returns:
        dict: 新创建的项目ID
    """
    logging.info(f"User {user_id} started copying template {template_id}")
    
    # 获取模板数据
    project_template = get_project_description_item(template_id)
    if not project_template:
        logging.error(f"User {user_id} failed to copy template {template_id}: template not found")
        return None
    
    generate_seed = random.randint(100000, 999999) #生成种子,用户生成图片或者视频
    
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    # current_time 是 utc时间，名称需要是用户本地时间
    format_time = mongo_instance.get_local_formatted_time(current_time)
    
    default_image_model_name = os.environ.get("IMAGE_MODEL_NAME", "runninghub")
    
    image_model_name = project_template.get('imageModelName', default_image_model_name)
    
    # 创建新项目数据结构
    new_project_id = mongo_instance.generate_object_id()
    new_project = {
        "_id": new_project_id,
        "user_id": user_id,
        "status": "active",
        "project_language": project_template.get('language', 'en-US'),
        "project_name": f"{project_template.get('name', 'new_project')}_{format_time}",
        "project_type": 1, #1 表示从模版复制
        "image_model_name": image_model_name,
        "style_type": project_template.get('storyBoardType', 0),
        "style_type_desc": project_template.get('storyBoardTypeDesc', ""),
        "picture_size": project_template.get('pictureSize', "16:9"),
        "image_size": project_template.get('imageSize', "1344x768"),
        "cover": project_template.get('cover', ""),
        "script_type": project_template.get('scriptType', 0),
        "script_content": project_template.get('content', ""),
        "times_and_culture": "",  # 从脚本中提取的年代和文化元素
        "times_and_culture_en": "",  # 英文版的年代和文化元素
        "has_shot": False,
        "has_role": False,
        "has_storyboard": False,
        "generate_seed": generate_seed,
        "shot_ids": [],  # 直接关联镜头ID
        "role_ids": [],
        "voiceover_model_name": "",  # 旁白的音效模型
        "last_updated_at": current_time,
        "created_at": current_time,
        "created_at_str": beijing_formatted_time
    }
    
    logging.info(f"User {user_id} created new project {new_project_id} from template {template_id}")
    
    image_model = create_image_model(image_model_name)

    # 复制模板中的角色
    role_template = get_project_role_item(template_id)
    all_roles = []
    all_role_resources = []
    template_role_id_map = {}  # 用于存储模板角色ID到新角色ID的映射
    role_resource_map = {}  # 用于存储角色ID到角色资源URL的映射
    
    if role_template and isinstance(role_template, list):
        logging.info(f"User {user_id} copying {len(role_template)} roles from template {template_id}")
        for idx, role_item in enumerate(role_template):
            new_role_id = mongo_instance.generate_object_id()
            template_role_id = role_item.get('roleId')
            if template_role_id:
                template_role_id_map[template_role_id] = new_role_id
            
            role_name = role_item.get('figureName', f"role_{idx + 1}")
            
            # 创建角色，确保包含所有必要字段
            new_role = {
                "_id": new_role_id,
                "user_id": user_id,
                "project_id": new_project_id,
                "status": "active",
                "role_name": role_name,
                "role_resource_ids": [],
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
            
            new_project["role_ids"].append(new_role_id)
            all_roles.append(new_role)
            
            if 'url' in role_item:
                new_role_resource_id = mongo_instance.generate_object_id()
                new_role_resource = {
                    "_id": new_role_resource_id,
                    "user_id": user_id,
                    "project_id": new_project_id,
                    "role_id": new_role_id,
                    "description": role_item.get('figureDesc', ""),
                    "description_en": role_item.get('enDesc', ""),
                    "image_model_name": image_model_name,
                    "style_type": new_project["style_type"],
                    "style_type_desc": new_project["style_type_desc"],
                    "image_size": image_model.get_role_image_size(),  # 角色采用固定尺寸
                    "generate_seed": generate_seed,
                    "generate_id": "",  # 生成ID
                    "generate_status": "done",  # 生成状态
                    "resource_url": role_item.get('url', ""),
                    "resource_prompt": "",
                    "voice_model_name": role_item.get('roleVoiceModelName', ""),
                    "face_image": role_item.get('faceImage', ""),
                    "projection_image": role_item.get('projectionImage', []),
                    "last_updated_at": current_time,
                    "created_at": current_time,
                    "created_at_str": beijing_formatted_time
                }

                new_role["selected_role_resource_id"] = new_role_resource_id
                new_role["role_resource_ids"].append(new_role_resource_id)
                all_role_resources.append(new_role_resource)
                
                # 存储角色资源URL，用于后续镜头中的角色引用
                role_resource_map[new_role_id] = {
                    "resource_id": new_role_resource_id,
                    "resource_url": new_role_resource["resource_url"]
                }
            
        if all_roles:
            new_project["has_role"] = True

    # 复制模板中的镜头    
    shot_template = get_project_shot_item(template_id)
    all_shots = []
    all_shot_resources = []
    
    if shot_template and isinstance(shot_template, list):
        logging.info(f"User {user_id} copying {len(shot_template)} shots from template {template_id}")
        for idx, shot_item in enumerate(shot_template):
            new_shot_id = mongo_instance.generate_object_id()
            
            # 处理角色信息
            selected_roles = []
            scene_desc = shot_item.get('scene_description', {})
            characters = scene_desc.get('characters', [])
            
            for character in characters:
                template_role_id = character.get('role_id')
                if template_role_id in template_role_id_map:
                    new_role_id = template_role_id_map[template_role_id]
                    
                    # 获取角色资源信息
                    role_resource_info = role_resource_map.get(new_role_id)
                    if role_resource_info:
                        selected_roles.append({
                            "role_id": new_role_id,
                            "action_and_emotion": character.get('action_and_emotion', ''),
                            "action_and_emotion_en": character.get('action_and_emotion_en', ''),
                        })
            
            # 处理台词
            dialogues = []
            for dialogue in shot_item.get('dialogues', []):
                role_id = dialogue.get('role_id')
                if role_id == 'voiceover':
                    dialogues.append({
                        "role_id": "voiceover",
                        "content": dialogue.get('content', '')
                    })
                elif role_id in template_role_id_map:
                    dialogues.append({
                        "role_id": str(template_role_id_map[role_id]),
                        "content": dialogue.get('content', '')
                    })
            
            # 创建新的镜头资源
            new_shot_resource_id = mongo_instance.generate_object_id()
            shot_resource = shot_item.get('shot_resource', {})
            new_shot_resource = {
                "_id": new_shot_resource_id,
                "user_id": user_id,
                "project_id": new_project_id,
                "shot_id": new_shot_id,
                "image_model_name": image_model_name,
                "style_type": new_project["style_type"],
                "style_type_desc": new_project["style_type_desc"],
                "image_size": new_project["image_size"],
                "generate_seed": generate_seed,
                "generate_id": "",
                "generate_status": "done",
                "resource_type": 1,  # 1表示图片
                "resource_url": shot_resource.get("shot_resource_url", ""),
                "resource_prompt": "",
                "is_HD": shot_resource.get("is_HD", ""),
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
            all_shot_resources.append(new_shot_resource)
            
            
            #解析shot_size
            size_values = shot_item.get("shot_size").get("size_values")
            shot_value = shot_item.get("shot_size").get("value")
            shot_size = size_values.index(shot_value)
            
            #解析camera_angle
            angle_values = shot_item.get("camera_angle").get("angle_values")
            angle_value = shot_item.get("camera_angle").get("value")
            camera_angle = angle_values.index(angle_value)
            
            #解析shot_type
            type_values = shot_item.get("shot_type").get("type_values")
            type_value = shot_item.get("shot_type").get("value")
            shot_type = type_values.index(type_value)
            
            #解析shot_time
            shot_time = shot_item.get("shot_time").get("value")
            
            # 创建新的镜头
            new_shot = {
                "_id": new_shot_id,
                "user_id": user_id,
                "project_id": new_project_id,
                "status": "active",
                "background": scene_desc.get('background', ""),
                "background_en": "",
                "selected_roles": selected_roles,
                "dialogues": dialogues,
                "selected_shot_resource_id": new_shot_resource_id,
                "shot_size": shot_size,
                "camera_angle": camera_angle,
                "shot_type": shot_type,
                "shot_time": shot_time,
                "shot_resource_ids": [new_shot_resource_id],
                "other_info": shot_item.get("other_info", []),
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
            
            all_shots.append(new_shot)
            new_project["shot_ids"].append(new_shot_id)
            
        if all_shots:
            new_project["has_shot"] = True
            new_project["has_storyboard"] = True
    
    # 如果项目封面为空，使用第一个镜头的资源作为封面
    if not new_project["cover"]:
        if all_shot_resources and all_shot_resources[0]["resource_url"]:
            new_project["cover"] = all_shot_resources[0]["resource_url"]
    
    try:
        # 开始批量插入数据
        # 1. 插入项目
        await mongo_instance.insert_one("projects", new_project)
        logging.info(f"User {user_id} inserted project {new_project_id} into database")
        
        # 2. 插入所有角色
        if all_roles:
            await mongo_instance.insert_many("roles", all_roles)
            logging.info(f"User {user_id} inserted {len(all_roles)} roles for project {new_project_id}")
        
        # 3. 插入所有角色资源
        if all_role_resources:
            await mongo_instance.insert_many("role_resources", all_role_resources)
            logging.info(f"User {user_id} inserted {len(all_role_resources)} role resources for project {new_project_id}")
        
        # 4. 插入所有镜头
        if all_shots:
            await mongo_instance.insert_many("shots", all_shots)
            logging.info(f"User {user_id} inserted {len(all_shots)} shots for project {new_project_id}")
        
        # 5. 插入所有镜头资源
        if all_shot_resources:
            await mongo_instance.insert_many("shot_resources", all_shot_resources)
            logging.info(f"User {user_id} inserted {len(all_shot_resources)} shot resources for project {new_project_id}")
        
        logging.info(f"User {user_id} successfully copied template {template_id} to project {new_project_id}")
        return new_project_id
    except Exception as e:
        logging.error(f"User {user_id} failed to copy template {template_id}: {str(e)}", exc_info=True)
        # 尝试清理已插入的数据
        try:
            await mongo_instance.delete_one("projects", {"_id": new_project_id})
            await mongo_instance.delete_many("roles", {"project_id": new_project_id})
            await mongo_instance.delete_many("role_resources", {"project_id": new_project_id})
            await mongo_instance.delete_many("shots", {"project_id": new_project_id})
            await mongo_instance.delete_many("shot_resources", {"project_id": new_project_id})
        except Exception as cleanup_error:
            logging.error(f"Failed to clean up after error: {str(cleanup_error)}")
        return None
    
#从数据库项目复制工程
async def copy_project_from_db(user_id, project_id):
    """
    根据项目ID复制一个新项目

    Args:
        user_id: 用户ID
        project_id: 项目ID

    Returns:
        str: 新创建的项目ID，失败返回None
    """
    logging.info(f"User {user_id} started copying project {project_id}")
    
    # 获取原项目数据
    original_project = await mongo_instance.find_one("projects", {"_id": project_id})
    if not original_project:
        logging.error(f"User {user_id} failed to copy project {project_id}: project not found")
        return None
    
    generate_seed = random.randint(100000, 999999) #生成种子,用户生成图片或者视频
    
    # 获取当前时间
    current_time, beijing_formatted_time, _ = mongo_instance.get_current_time()
    
    # current_time 是 utc时间，名称需要是用户本地时间
    format_time = mongo_instance.get_local_formatted_time(current_time)
    
    #新项目名称
    new_project_name = f"{original_project.get('project_name', 'new_project')}_{format_time}"
    
    default_image_model_name = os.environ.get("IMAGE_MODEL_NAME", "runninghub")
    
    image_model_name = original_project.get("image_model_name", default_image_model_name)
    
    # 创建新项目数据结构
    new_project_id = mongo_instance.generate_object_id()
    new_project = {
        "_id": new_project_id,
        "user_id": user_id,
        "status": "active",
        "project_language": original_project.get("project_language", "zh-CN"),
        "project_name": new_project_name,
        "project_type": 2,  # 2表示项目复制
        "image_model_name": image_model_name,
        "style_type": original_project.get("style_type", 1),
        "style_type_desc": original_project.get("style_type_desc", ""),
        "picture_size": original_project.get("picture_size", "16:9"),
        "image_size": original_project.get("image_size", "1344x768"),
        "cover": original_project.get("cover", ""),
        "script_type": original_project.get("script_type", 0),
        "script_content": original_project.get("script_content", ""),
        "times_and_culture": original_project.get("times_and_culture", ""),
        "times_and_culture_en": original_project.get("times_and_culture_en", ""),
        "has_shot": False,
        "has_role": False,
        "has_storyboard": False,
        "generate_seed": generate_seed,
        "shot_ids": [],
        "role_ids": [],
        "voiceover_model_name": original_project.get("voiceover_model_name", ""),
        "last_updated_at": current_time,
        "created_at": current_time,
        "created_at_str": beijing_formatted_time
    }
    
    logging.info(f"User {user_id} created new project {new_project_id} from project {project_id}")
    
    image_model = create_image_model(image_model_name)

    # 复制原项目中的角色
    all_roles = []
    all_role_resources = []
    original_role_id_map = {}  # 用于存储原角色ID到新角色ID的映射
    role_resource_map = {}  # 用于存储角色ID到角色资源URL的映射
    
    # 按照原项目中role_ids的顺序复制角色
    for original_role_id in original_project.get("role_ids", []):
        role = await mongo_instance.find_one("roles", {"_id": original_role_id, "status": "active"})
        if not role:
            continue
            
        new_role_id = mongo_instance.generate_object_id()
        original_role_id_map[str(original_role_id)] = new_role_id
        
        # 创建新角色
        new_role = {
            "_id": new_role_id,
            "user_id": user_id,
            "project_id": new_project_id,
            "status": "active",
            "role_name": role.get("role_name", ""),
            "role_resource_ids": [],
            "last_updated_at": current_time,
            "created_at": current_time,
            "created_at_str": beijing_formatted_time
        }
        
        # 如果原角色有选中的资源，先记录下来
        if "selected_role_resource_id" in role:
            new_role["selected_role_resource_id"] = None  # 先设置为None，后面会更新
        
        new_project["role_ids"].append(new_role_id)
        all_roles.append(new_role)
        
        # 复制角色资源
        original_role_resources = await mongo_instance.find_many(
            "role_resources", 
            {"role_id": original_role_id}
        )
        
        for role_resource in original_role_resources:
            new_role_resource_id = mongo_instance.generate_object_id()
            new_role_resource = {
                "_id": new_role_resource_id,
                "user_id": user_id,
                "project_id": new_project_id,
                "role_id": new_role_id,
                "description": role_resource.get("description", ""),
                "description_en": role_resource.get("description_en", ""),
                "image_model_name": image_model_name,
                "style_type": role_resource.get("style_type", new_project["style_type"]),
                "style_type_desc": role_resource.get("style_type_desc", new_project["style_type_desc"]),
                "image_size": role_resource.get("image_size", image_model.get_role_image_size()),
                "generate_seed": generate_seed,
                "generate_id": role_resource.get("generate_id", ""),
                "generate_status": role_resource.get("generate_status", "done"),
                "resource_url": role_resource.get("resource_url", ""),
                "resource_prompt": role_resource.get("resource_prompt", ""),
                "voice_model_name": role_resource.get("voice_model_name", ""),
                "face_image": role_resource.get("face_image", ""),
                "projection_image": role_resource.get("projection_image", []),
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
            
            new_role["role_resource_ids"].append(new_role_resource_id)
            all_role_resources.append(new_role_resource)
            
            # 如果是选中的资源，更新角色的选中资源ID
            if str(role_resource.get("_id")) == str(role.get("selected_role_resource_id")):
                new_role["selected_role_resource_id"] = new_role_resource_id
            
            # 存储角色资源信息，用于后续镜头中的角色引用
            role_resource_map[new_role_id] = {
                "resource_id": new_role_resource_id,
                "resource_url": new_role_resource["resource_url"]
            }
            
    if all_roles:
        new_project["has_role"] = True

    # 复制原项目中的镜头
    all_shots = []
    all_shot_resources = []
    
    # 按照原项目中shot_ids的顺序复制镜头
    for original_shot_id in original_project.get("shot_ids", []):
        shot = await mongo_instance.find_one("shots", {"_id": original_shot_id, "status": "active"})
        if not shot:
            continue
            
        new_shot_id = mongo_instance.generate_object_id()
        
        # 处理角色信息
        selected_roles = []
        for role in shot.get("selected_roles", []):
            original_role_id = role.get("role_id")
            if str(original_role_id) in original_role_id_map:
                new_role_id = original_role_id_map[str(original_role_id)]
                
                # 获取角色资源信息
                role_resource_info = role_resource_map.get(new_role_id)
                if role_resource_info:
                    selected_roles.append({
                        "role_id": new_role_id,
                        "action_and_emotion": role.get("action_and_emotion", ""),
                        "action_and_emotion_en": role.get("action_and_emotion_en", ""),
                    })
        
        # 处理台词
        dialogues = []
        for dialogue in shot.get("dialogues", []):
            role_id = dialogue.get("role_id")
            if role_id == "voiceover":
                dialogues.append({
                    "role_id": "voiceover",
                    "content": dialogue.get("content", "")
                })
            elif role_id in original_role_id_map:
                dialogues.append({
                    "role_id": str(original_role_id_map[role_id]),
                    "content": dialogue.get("content", "")
                })
        
        # 创建新的镜头资源
        original_shot_resources = await mongo_instance.find_many(
            "shot_resources", 
            {"shot_id": original_shot_id}
        )
        
        shot_resource_ids = []
        selected_shot_resource_id = None
        
        for shot_resource in original_shot_resources:
            new_shot_resource_id = mongo_instance.generate_object_id()
            new_shot_resource = {
                "_id": new_shot_resource_id,
                "user_id": user_id,
                "project_id": new_project_id,
                "shot_id": new_shot_id,
                "image_model_name": image_model_name,
                "style_type": shot_resource.get("style_type", new_project["style_type"]),
                "style_type_desc": shot_resource.get("style_type_desc", new_project["style_type_desc"]),
                "image_size": shot_resource.get("image_size", new_project["image_size"]),
                "generate_seed": generate_seed,
                "generate_id": shot_resource.get("generate_id", ""),
                "generate_status": shot_resource.get("generate_status", "done"),
                "resource_type": shot_resource.get("resource_type", 1),
                "resource_url": shot_resource.get("resource_url", ""),
                "resource_prompt": shot_resource.get("resource_prompt", ""),
                "is_HD": shot_resource.get("is_HD", False),
                "last_updated_at": current_time,
                "created_at": current_time,
                "created_at_str": beijing_formatted_time
            }
            all_shot_resources.append(new_shot_resource)
            shot_resource_ids.append(new_shot_resource_id)
            
            # 如果是选中的资源，记录ID和URL
            if str(shot_resource.get("_id")) == str(shot.get("selected_shot_resource_id")):
                selected_shot_resource_id = new_shot_resource_id
        
        # 如果没有找到选中的资源，使用第一个资源
        if not selected_shot_resource_id and shot_resource_ids:
            selected_shot_resource_id = shot_resource_ids[0]
        
        # 创建新的镜头
        new_shot = {
            "_id": new_shot_id,
            "user_id": user_id,
            "project_id": new_project_id,
            "status": "active",
            "background": shot.get("background", ""),
            "background_en": shot.get("background_en", ""),
            "selected_roles": selected_roles,
            "dialogues": dialogues,
            "selected_shot_resource_id": selected_shot_resource_id,
            "shot_size": shot.get("shot_size", 1),  # 数字表示景别
            "camera_angle": shot.get("camera_angle", 0),  # 数字表示摄像机角度
            "shot_type": shot.get("shot_type", 0),  # 数字表示摄影机运动
            "shot_time": shot.get("shot_time", 3),  # 数字表示镜头时长(秒)
            "shot_resource_ids": shot_resource_ids,
            "other_info": shot.get("other_info", ""),
            "last_updated_at": current_time,
            "created_at": current_time,
            "created_at_str": beijing_formatted_time
        }
        
        all_shots.append(new_shot)
        new_project["shot_ids"].append(new_shot_id)
    
    if all_shots:
        new_project["has_shot"] = True
        new_project["has_storyboard"] = True
    
    # 如果项目封面为空，使用第一个镜头的资源作为封面
    if not new_project["cover"]:
        if all_shot_resources and all_shot_resources:
            new_project["cover"] = all_shot_resources[0]["resource_url"]
    
    try:
        # 开始批量插入数据
        # 1. 插入项目
        await mongo_instance.insert_one("projects", new_project)
        logging.info(f"User {user_id} inserted project {new_project_id} into database")
        
        # 2. 插入所有角色
        if all_roles:
            await mongo_instance.insert_many("roles", all_roles)
            logging.info(f"User {user_id} inserted {len(all_roles)} roles for project {new_project_id}")
        
        # 3. 插入所有角色资源
        if all_role_resources:
            await mongo_instance.insert_many("role_resources", all_role_resources)
            logging.info(f"User {user_id} inserted {len(all_role_resources)} role resources for project {new_project_id}")
        
        # 4. 插入所有镜头
        if all_shots:
            await mongo_instance.insert_many("shots", all_shots)
            logging.info(f"User {user_id} inserted {len(all_shots)} shots for project {new_project_id}")
        
        # 5. 插入所有镜头资源
        if all_shot_resources:
            await mongo_instance.insert_many("shot_resources", all_shot_resources)
            logging.info(f"User {user_id} inserted {len(all_shot_resources)} shot resources for project {new_project_id}")
        
        logging.info(f"User {user_id} successfully copied project {project_id} to project {new_project_id}")
        
        return new_project_id,new_project_name
    except Exception as e:
        logging.error(f"User {user_id} failed to copy project {project_id}: {str(e)}", exc_info=True)
        # 尝试清理已插入的数据
        try:
            await mongo_instance.delete_one("projects", {"_id": new_project_id})
            await mongo_instance.delete_many("roles", {"project_id": new_project_id})
            await mongo_instance.delete_many("role_resources", {"project_id": new_project_id})
            await mongo_instance.delete_many("shots", {"project_id": new_project_id})
            await mongo_instance.delete_many("shot_resources", {"project_id": new_project_id})
        except Exception as cleanup_error:
            logging.error(f"Failed to clean up after error: {str(cleanup_error)}")
        return None,""
    