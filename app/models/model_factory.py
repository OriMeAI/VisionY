import os

"""
语言模型接入
"""

def create_llm_model(name:str = None):
    """
    创建语言模型
    """
    model_name = name if name else os.environ.get("LLM_MODEL_NAME", "openrouter")
    
    if model_name == "volcengine":
        from.llm.llm_volcengine import llm_volcengine_instance
        return llm_volcengine_instance
    
    if model_name == "openrouter":
        from.llm.llm_openrouter import llm_openrouter_instance
        return llm_openrouter_instance
    else:
        pass

def create_image_model(name:str = None):
    """
    创建图片模型
    调用generate_image 或者 repaint_image 或者 hd_resolution 返回结果说明
    generate_result = {"code":2, "generate_id":"","image_prompt":"" ,"message":"credits is not enough"}
    # code 值说明 0 代表成功 1 代表失败 2 代表用户积分不足 3 商业API官方的账号积分不足 4 代表上传生成图片失败 5 代表上传蒙版图片失败
    
    # generate_image, repaint_image, hd_resolution 三个函数的参数说明 眼下是旧的逻辑
    # generate_image(prompt, used_type, style_type=1, size="576x1024", n=1, seed=1234)
    # repaint_image(prompt, used_type, image_url, mask_data, style_type=1, size="576x1024", n=1, seed=1234)
    # hd_resolution(image_url, used_type, style_type=1)
    
    # 需要将结果检查放到逻辑层进行, 先调用下列函数
    # generate_shot_image_with_no_character, repaint_image, hd_resolution 
    # 然后调用 check_image_status, 检查生成结果
    # check_result 的结果 -1 初始化的值 0 成功 1 进行中 2 积分不足 3 上传图片失败 4 任务失败 5 查询异常
    
    
    初期GPU用量少可以哦那个 comfy.icu https://comfy.icu/pricing
    一个月差不多是 16800元 0.0009美元/秒 23.33元/小时
    
    后期GPU用量大可以用ali，
    一个月最少是 3888元 0.0015元/秒 5.4元/小时，最多是 6480元 0.0025元/秒 9元/小时
    
    runninghub https://www.runninghub.cn/call-api
    费用 共享模式 ¥7 /小时，按秒计费 大显存Plus模式 ¥10.5 /小时，按秒计费 。独占 24G显存机器 ¥1500 /路/月 2.08元/小时，48G显存机器 ¥2250 /路/月，3.125元/小时
    
    runcomfy https://www.runcomfy.com/pricing?tab=comfyui
    价格 24G 1.75美元/小时 12.25元/小时 每月 8820元 。pro 1.39美元/小时 9.73元/小时 每月 7005元每月
    
    """
    
    model_name = name if name else os.environ.get("IMAGE_MODEL_NAME", "runninghub")
    
    if model_name == "runninghub":
        from.image.image_runninghub import image_runninghub_instance
        return image_runninghub_instance
    elif model_name == "liblib":
        from.image.image_liblib import image_liblib_instance
        return image_liblib_instance
    else:
        pass
    
def create_translator_model(name:str = "volcengine"):
    """
    创建翻译模型
    """
    if name == "volcengine":
        from.translator.translator_volcengine import TranslatorVolcengine
        return TranslatorVolcengine()
    else:
        pass
    
def create_cdn_instance():
    """
    创建cdn模型
    """
    #对于cloudflare 和 tencent cos 进行封装
    # from .cdn.tencent_cos import tencent_cos_instance
    # return tencent_cos_instance
    # from .cdn.cloudflare import cloudflare_instance
    # return cloudflare_instance
    from .cdn.aliyun_oss import aliyun_oss_instance
    return aliyun_oss_instance