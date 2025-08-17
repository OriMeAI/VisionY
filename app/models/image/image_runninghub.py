
import os
import logging
import aiohttp
import json
import requests
import asyncio
import time
from contextlib import asynccontextmanager

from app.models.model_factory import create_cdn_instance
from app.collections.credits_helper import check_for_credits,deduct_used_credits
from app.utils.redis_client import redis_instance

from .image_base.image_base import ImageBase

from .runninghub_api import flux_dev_generate_character_with_lora_api
from .runninghub_api import kontext_pro_generate_shot_with_characters_api
from .runninghub_api import kontext_pro_mask_edit_api
from .runninghub_api import kontext_pro_text_edit_api
from .runninghub_api import kontext_dev_simple_hd_api
from .runninghub_api import kontext_pro_generate_shot_no_characters_api

"""
文档地址
https://www.runninghub.cn/runninghub-api-doc/

视觉盲盒 给各种图片做风格化，一共有35种风格
https://www.runninghub.cn/ai-detail/1927605182249734145

小说推文 短视频分镜配图 [内含 文生图/局部重绘(修手)/高清放大] 工作流
https://www.runninghub.cn/post/1934770233473474562

OmniConsistency全能转绘王！22种风格任选，转绘不再难
https://www.runninghub.cn/post/1928695867409338370


1 创建任务
https://www.runninghub.cn/runninghub-api-doc/api-276613249

请求地址
POST https://www.runninghub.cn/task/openapi/create

2 查询任务生成结果
https://www.runninghub.cn/runninghub-api-doc/api-276613253

3 计费说明
0.2RH/秒 24G， 0.4RH/秒，48G。
flux pro 0.14元/张，flux max 0.28元/张

trigger_word来自于 chatgpt
https://chatgpt.com/c/68745c07-ec80-800e-bcf2-77f1bd273344

"""
class ImageRunningHub(ImageBase):
    """
    星琉 AI 图像生成模型实现
    """
    
    _instance = None    

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        初始化星琉图像模型
        """
        self.model_name = "runninghub"
        self._max_concurrent_requests = int(os.environ.get("RUNNINGHUB_MAX_CONCURRENT", "10"))  # 最大并发请求数
        self._redis_key = os.environ.get("RUNNINGHUB_REDIS_KEY", "runninghub:concurrent_requests")
        self._request_timeout = int(os.environ.get("RUNNINGHUB_REQUEST_TIMEOUT", "300"))  # 请求超时时间（秒）
        
        # 从环境变量获取密钥
        # self.api_key = os.environ.get("RUNNINGHUB_CONSUMER_API_KEY", "")
        self.api_key = os.environ.get("RUNNINGHUB_SHARE_ORG_API_KEY", "")
        # self.api_key = os.environ.get("RUNNINGHUB_ORG_API_KEY", "")
        # 'www.runninghub.cn' or www.runninghub.ai'
        # self.api_endpoint = 'www.runninghub.cn' 
        self.api_endpoint = 'www.runninghub.cn' 
        self.instance_type = "plus" # "" 或者 "plus" 若希望发起plus任务到48G显存机器上执行 只对用户API或者企业共享API有效
        self.headers = {
            'Host': self.api_endpoint,
            'Content-Type': 'application/json'
        }
        
        # 添加超时配置
        self.timeout = aiohttp.ClientTimeout(
            total=60,      # 总超时时间60秒
            connect=10,    # 连接超时10秒
            sock_read=30   # 读取超时30秒
        )
        
        #重试次数
        self.max_retries = 3
        
        # 检查任务状态超时时间, 3分钟
        self.check_timeout = 180
                
        logging.info(f"Initialized RunningHub ImageModel")
        
    async def _acquire_request_slot(self):
        """
        获取请求槽位（跨进程并发控制）
        
        Returns:
            str: 请求ID，用于后续释放槽位
        """
        return await redis_instance.acquire_request_slot(
            self._redis_key, 
            self._max_concurrent_requests, 
            self._request_timeout
        )
    
    async def _release_request_slot(self, request_id: str):
        """
        释放请求槽位
        
        Args:
            request_id: 请求ID
        """
        await redis_instance.release_request_slot(self._redis_key, request_id)
                                        
    def get_model_name(self):
        """
        获取模型名称

        Returns:
            模型名称
        """
        return self.model_name
                                    
    async def generate_character_image(self, used_type,prompt, style_type=1, size="576x1024", n=1, seed=1234):
        """
        生成图像 - RunningHub API实现
        
        Args:
            prompt: 图像生成提示词
            used_type: 使用类型
            style_type: 风格类型ID
            size: 图像尺寸，格式为"宽x高"
            n: 生成图像数量
            seed: 随机种子
            
        Returns:
            dict: 生成结果，包含状态码、消息和图像URL
        """
        # 0 代表成功 1 代表失败 2 代表用户积分不足 3 商业API官方的账号积分不足 4 代表上传图片失败
        generate_result = {"code": -1, "generate_id": "", "image_prompt": "", "msg": "something is wrong"}
        
        has_credits = await check_for_credits()
        if not has_credits:
            generate_result["code"] = 2
            generate_result["msg"] = "credits is not enough"
            return generate_result
        
        # 解析尺寸
        if "x" in size:
            width, height = map(int, size.split("x"))
        else:
            # Default size if not specified correctly
            width, height = 576, 1024
                    
        image_style,image_prompt = self.get_character_style_prompt(style_type,prompt)
        generate_result["image_prompt"] = image_prompt

        extra_info = {}
        
        # 构建API请求
        url = f"https://{self.api_endpoint}/task/openapi/create"  # 根据实际API端点调整
        
        api_info = flux_dev_generate_character_with_lora_api.get_workflow_api(seed,image_style,image_prompt,width,height)
        extra_info["extra_credits"] = api_info["extra_credits"]
                
        # 构建RunningHub ComfyUI工作流数据
        payload = {
            "apiKey":self.api_key,
            "workflowId": api_info["workflowId"], 
            "workflow": json.dumps(api_info["workflow"],ensure_ascii=False),
            "addMetadata":  False, #是否在图片中写入元信息（如提示词）
            "usePersonalQueue":True, #独占类型任务是否入队
        }
                                
        try:
            # 获取并发槽位
            request_id = await self._acquire_request_slot()
            
            for attempt in range(self.max_retries):
                try:
                    async with aiohttp.ClientSession(timeout=self.timeout) as session:
                        async with session.post(url=url, headers=self.headers, json=payload) as response:
                            if response.status != 200:
                                # 获取详细错误信息
                                try:
                                    warning_detail = await response.text()
                                    warning_msg = f"Submit character task failed: HTTP {response.status}, Detail: {warning_detail}"
                                except:
                                    warning_msg = f"Submit character task failed: HTTP {response.status}"
                                
                                logging.warning(warning_msg)

                            else:
                                result = await response.json()
                                                    
                                if result.get('code') == 0:  # 根据实际API响应格式调整
                                    generate_result["code"] = 0
                                    # 获取任务ID
                                    generate_id = result.get('data', {}).get('taskId')
                                    generate_result["generate_id"] = generate_id
                                    
                                    logging.info(f"RunningHub character task submitted successfully, generate_id: {generate_id}")
                                    
                                    #check generate result
                                    check_result = await self.check_generate_status(used_type, generate_id,extra_info)
                                    check_code = check_result["code"]
                                    check_message = check_result["msg"]
                                                                
                                    if check_code == 0: #成功
                                        generate_result["code"] = 0                            
                                        generate_result["image_url"] = check_result["image_url"]
                                        return generate_result
                                    else:                                    
                                        generate_result["code"] = check_code
                                        generate_result["msg"] = check_message        
                                        return generate_result
                                    
                except Exception as e:
                    # 其他异常
                    warning_msg = f"Submit character task warning: {str(e)}"
                    logging.warning(warning_msg)
                    
                if attempt == self.max_retries - 1:  # 最后一次重试
                    error_msg = f"Submit character task failed after {self.max_retries} attempts"
                    generate_result["code"] = 5
                    generate_result["msg"] = error_msg
                    logging.error(error_msg)
                    return generate_result
                else:
                    logging.warning(f"Submit character task attempt {attempt + 1}, retrying...")
                    await asyncio.sleep(2 ** attempt)  # 指数退避
        
        except Exception as e:
            error_msg = f"Generate character image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg, exc_info=True)
            return generate_result
        
        finally:
            # 确保在方法完全返回时释放并发槽位
            await self._release_request_slot(request_id)
          
    async def generate_shot_image_with_characters(self,used_type,prompt,style_type,size, seed,first_character,second_character,third_character):
        """
        生成图像 - RunningHub API实现
        
        Args:
            prompt: 图像生成提示词
            used_type: 使用类型
            style_type: 风格类型ID
            size: 图像尺寸，格式为"宽x高"
            n: 生成图像数量
            seed: 随机种子
            
        Returns:
            dict: 生成结果，包含状态码、消息和图像URL
        """
                
        empty_scene = False
        
        default_role_image_url = self.get_default_role_blank_url()
        
        # print(f"default_role_image_url is {default_role_image_url}")
        
        if first_character is None:
            empty_scene = True 
            first_character = default_role_image_url
            second_character = default_role_image_url 
            third_character = default_role_image_url
        elif second_character is None:
            first_character = self.get_cn_resource_url(first_character)
            second_character = default_role_image_url 
            third_character = default_role_image_url
        elif third_character is None:
            first_character = self.get_cn_resource_url(first_character)
            second_character = self.get_cn_resource_url(second_character)
            third_character = default_role_image_url
        else:
            first_character = self.get_cn_resource_url(first_character)
            second_character = self.get_cn_resource_url(second_character)
            third_character = self.get_cn_resource_url(third_character)
                
        # print(f"first_character is {first_character}")
        # print(f"second_character is {second_character}")
        # print(f"third_character is {third_character}")
        
        # 0 代表成功 1 代表失败 2 代表用户积分不足 3 商业API官方的账号积分不足 4 代表上传图片失败
        generate_result = {"code": -1, "generate_id": "", "image_prompt": "", "msg": "something is wrong"}
        
        has_credits = await check_for_credits()
        if not has_credits:
            generate_result["code"] = 2
            generate_result["msg"] = "credits is not enough"
            return generate_result
        
        # 解析尺寸
        if "x" in size:
            width, height = map(int, size.split("x"))
        else:
            # Default size if not specified correctly
            width, height = 1024, 1024
                    
        #解析 aspect_ratio            
        aspect_ratio = self.get_aspect_ratio(size)
                
        image_style,image_prompt = self.get_shot_style_prompt(style_type,prompt,empty_scene)      
        
        extra_info = {}
        
        url = f"https://{self.api_endpoint}/task/openapi/create"  # 根据实际API端点调整
        
        if empty_scene:
            api_info = kontext_pro_generate_shot_no_characters_api.get_workflow_api(seed,aspect_ratio,image_prompt)
        else: 
            api_info = kontext_pro_generate_shot_with_characters_api.get_workflow_api(seed,aspect_ratio,image_prompt,first_character,second_character,third_character)  
                                    
        extra_info["extra_credits"] = api_info["extra_credits"]
        extra_info["need_parse_url"] = api_info["need_parse_url"]
                    
        # 构建RunningHub ComfyUI工作流数据
        payload = {
            "apiKey":self.api_key,
            "workflowId": api_info["workflowId"], 
            "workflow": json.dumps(api_info["workflow"],ensure_ascii=False),
            "addMetadata":  False, #是否在图片中写入元信息（如提示词）
            "usePersonalQueue":True, #独占类型任务是否入队
        }
                                
        try:        
            # 获取并发槽位
            request_id = await self._acquire_request_slot()
            
            for attempt in range(self.max_retries):
                
                logging.debug(f"Submit shot task, attempt {attempt + 1}")
                try:
                    async with aiohttp.ClientSession(timeout=self.timeout) as session:
                        async with session.post(url=url, headers=self.headers, json=payload) as response:
                            if response.status != 200:
                                # 获取详细错误信息
                                try:
                                    warning_detail = await response.text()
                                    warning_msg = f"Submit shot task failed: HTTP {response.status}, Detail: {warning_detail}"
                                except:
                                    warning_msg = f"Submit shot task failed: HTTP {response.status}"
                                    
                                logging.warning(warning_msg)
                            else:
                    
                                result = await response.json()
                                                    
                                if result.get('code') == 0:  # 根据实际API响应格式调整
                                    generate_result["code"] = 0
                                    # 获取任务ID
                                    generate_id = result.get('data', {}).get('taskId')
                                    generate_result["generate_id"] = generate_id
                                    
                                    logging.info(f"RunningHub shot task submitted successfully, generate_id: {generate_id}")
                                                            
                                    #check generate result
                                    check_result = await self.check_generate_status(used_type, generate_id,extra_info)
                                    check_code = check_result["code"]
                                    check_message = check_result["msg"]
                                                                
                                    if check_code == 0: #成功
                                        generate_result["code"] = 0                            
                                        generate_result["image_url"] = check_result["image_url"]
                                        return generate_result
                                    else:                                    
                                        generate_result["code"] = check_code
                                        generate_result["msg"] = check_message
                                        return generate_result
                    
                except Exception as e:
                    # 其他异常
                    warning_msg = f"Submit shot task warning: {str(e)}"
                    logging.warning(warning_msg)
                    
                if attempt == self.max_retries - 1:  # 最后一次重试
                    error_msg = f"Submit shot task failed after {self.max_retries} attempts"
                    generate_result["code"] = 5
                    generate_result["msg"] = error_msg
                    logging.error(error_msg)
                    return generate_result
                else:
                    logging.warning(f"Submit shot task attempt {attempt + 1}, retrying...")
                    await asyncio.sleep(2 ** attempt)  # 指数退避

        except Exception as e:
            error_msg = f"Generate shot image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg, exc_info=True)
            return generate_result
        
        finally:
            # 确保在方法完全返回时释放并发槽位
            await self._release_request_slot(request_id)
   
    #进行重绘
    async def repaint_image(self,used_type,seed, style_type, size, prompt,base_image, mask_data = ""):
        """
        重绘图像

        Args:
            prompt: 图像生成提示词
            base_image: 原始图像URL
            mask_data: 蒙版数据
        Returns:
            dict: 生成结果，包含状态码、消息和图像URL
        """
        
        # -1 默认值 0 代表成功 1 代表失败 2 代表用户积分不足
        generate_result = {"code":-1, "generate_id":"","image_prompt":"" ,"msg":"something is wrong"}
        
        has_credits = await check_for_credits()
        if not has_credits:
            generate_result["code"] = 2
            generate_result["msg"] = "credits is not enough"
            return generate_result
        
        base_image = self.get_cn_resource_url(base_image)
        
        # 根据style_type从IMAGE_STYLE_LIST获取相关参数
        image_style = None

        for style in self.image_style_list:
            if style["type_id"] == style_type:
                image_style = style["image_style"]
                break
        
        # 如果找不到对应的风格，使用默认值
        if image_style is None:
            logging.warning(f"Can not find style {style_type}, use default style")
            style = self.image_style_list[0]
            image_style = style["image_style"]
                    
        # image_prompt = f"{image_style}, {prompt}"
        image_prompt = prompt
        generate_result["image_prompt"] = image_prompt
        extra_info = {}
        
        logging.info(f"generate_repaint_image, image_prompt is {image_prompt}")
        
        # 解析尺寸
        if "x" in size:
            width, height = map(int, size.split("x"))
        else:
            # Default size if not specified correctly
            width, height = 1024, 1024
                
        #解析 aspect_ratio            
        aspect_ratio = self.get_aspect_ratio(size)
                
        if mask_data:
            #调用cloudflare上传图片
            cdn_instance = create_cdn_instance()
            upload_result = await cdn_instance.upload_base64(mask_data, "mask_data.png")
            if upload_result["status"] != "success":
                logging.info(f"upload mask_data, upload_result is {upload_result}")
                generate_result["code"] = 5
                generate_result["msg"] = "upload mask_data failed"
                return generate_result
            else:
                mask_image = upload_result["resource_url"]
                # 局部重绘（有蒙版）
                logging.info(f"Repaint mask data uploaded successfully, URL: {mask_image}")
                mask_image = self.get_cn_resource_url(mask_image)
                api_info = kontext_pro_mask_edit_api.get_workflow_api(seed, aspect_ratio,image_prompt,base_image,mask_image)
                extra_info["extra_credits"] = api_info["extra_credits"]
                extra_info["need_parse_url"] = api_info["need_parse_url"]
        else:      
           # 全图重绘（无蒙版）                                            
            api_info = kontext_pro_text_edit_api.get_workflow_api(seed,aspect_ratio,image_prompt,base_image)
            extra_info["extra_credits"] = api_info["extra_credits"]
            extra_info["need_parse_url"] = api_info["need_parse_url"]
            
        # 构建API请求
        url = f"https://{self.api_endpoint}/task/openapi/create"  # 根据实际API端点调整
        
        # 构建RunningHub ComfyUI工作流数据
        payload = {
            "apiKey":self.api_key,
            "workflowId": api_info["workflowId"], 
            "workflow": json.dumps(api_info["workflow"],ensure_ascii=False),
            "addMetadata":  False, #是否在图片中写入元信息（如提示词）
            "usePersonalQueue":True, #独占类型任务是否入队
        }
                                    
        try:                        
            # 获取并发槽位
            request_id = await self._acquire_request_slot()
            
            for attempt in range(self.max_retries):
                try:    
                    async with aiohttp.ClientSession(timeout=self.timeout) as session:
                        async with session.post(url=url, headers=self.headers, json=payload) as response:
                            if response.status != 200:
                                # 获取详细错误信息
                                try:
                                    warning_detail = await response.text()
                                    warning_msg = f"Submit repaint task failed: HTTP {response.status}, Detail: {warning_detail}"
                                except:
                                    warning_msg = f"Submit repaint task failed: HTTP {response.status}"
                            
                                logging.warning(warning_msg)
                        
                            else:
                    
                                result = await response.json()
                                                    
                                if result.get('code') == 0:  # 根据实际API响应格式调整
                                    generate_result["code"] = 0
                                    # 获取任务ID
                                    generate_id = result.get('data', {}).get('taskId')
                                    generate_result["generate_id"] = generate_id
                                    
                                    logging.info(f"RunningHub repaint task submitted successfully, generate_id: {generate_id}")
                                                            
                                    #check generate result
                                    check_result = await self.check_generate_status(used_type, generate_id,extra_info)
                                    check_code = check_result["code"]
                                    check_message = check_result["msg"]
                                                                
                                    if check_code == 0: #成功
                                        generate_result["code"] = 0                            
                                        generate_result["image_url"] = check_result["image_url"]
                                        return generate_result
                                    else:                                    
                                        generate_result["code"] = check_code
                                        generate_result["msg"] = check_message     
                                        return generate_result

                except Exception as e:
                    # 其他异常
                    warning_msg = f"Submit repaint task warning: {str(e)}"
                    logging.warning(warning_msg)
                    
                if attempt == self.max_retries - 1:  # 最后一次重试
                    error_msg = f"Submit repaint task failed after {self.max_retries} attempts"
                    generate_result["code"] = 5
                    generate_result["msg"] = error_msg
                    logging.error(error_msg)
                    return generate_result
                else:
                    logging.warning(f"Submit repaint task attempt {attempt + 1}, retrying...")
                    await asyncio.sleep(2 ** attempt)  # 指数退避
        
        except Exception as e:
            error_msg = f"Generate repaint image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg, exc_info=True)
            return generate_result
        
        finally:
            # 确保在方法完全返回时释放并发槽位
            await self._release_request_slot(request_id)
               
    #两倍细节放大
    async def hd_resolution(self,used_type,seed, style_type, prompt, image_url):
        """
        图像两倍放大

        Args:
            image_url: 原始图像URL
            seed: 随机种子
        Returns:
            dict: 生成结果，包含状态码、消息和图像URL
        """
        
        # 0 代表成功 1 代表失败 2 代表用户积分不足 3 商业API官方的账号积分不足 4 代表上传图片失败
        generate_result = {"code": -1, "generate_id": "", "image_prompt": "", "msg": "something is wrong"}
        
        has_credits = await check_for_credits()
        if not has_credits:
            generate_result["code"] = 2
            generate_result["msg"] = "credits is not enough"
            return generate_result
        
        image_url = self.get_cn_resource_url(image_url)
                
        # 根据style_type从IMAGE_STYLE_LIST获取相关参数
        image_style = None

        for style in self.image_style_list:
            if style["type_id"] == style_type:
                image_style = style["image_style"]
                break
        
        # 如果找不到对应的风格，使用默认值
        if image_style is None:
            logging.warning(f"Can not find style {style_type}, use default style")
            style = self.image_style_list[0]
            image_style = style["image_style"]
                    
        # image_prompt = f"{image_style}, {prompt}"
        image_prompt = prompt
        generate_result["image_prompt"] = image_prompt
        extra_info = {}
        
        logging.info(f"generate_hd_resolution_image, image_prompt is {image_prompt}")
        
        # 构建API请求
        url = f"https://{self.api_endpoint}/task/openapi/create"  # 根据实际API端点调整
        
        api_info = kontext_dev_simple_hd_api.get_workflow_api(seed,image_prompt,image_url)
        extra_info["extra_credits"] = api_info["extra_credits"]
                
        # 构建RunningHub ComfyUI工作流数据
        payload = {
            "apiKey":self.api_key,
            "workflowId": api_info["workflowId"], 
            "workflow": json.dumps(api_info["workflow"],ensure_ascii=False),
            "addMetadata":  False, #是否在图片中写入元信息（如提示词）
            "usePersonalQueue":True, #独占类型任务是否入队
        }
                        
        try:
            # 获取并发槽位
            request_id = await self._acquire_request_slot()
            
            for attempt in range(self.max_retries):
                try:
                    async with aiohttp.ClientSession(timeout=self.timeout) as session:
                        async with session.post(url=url, headers=self.headers, json=payload) as response:
                            if response.status != 200:
                                # 获取详细错误信息
                                try:
                                    warning_detail = await response.text()
                                    warning_msg = f"Submit hd_resolution task failed: HTTP {response.status}, Detail: {warning_detail}"
                                except:
                                    warning_msg = f"Submit hd_resolution task failed: HTTP {response.status}"
                                    
                                logging.warning(warning_msg)
                                                            
                            else:
                                result = await response.json()
                                                    
                                if result.get('code') == 0:  # 根据实际API响应格式调整
                                    generate_result["code"] = 0
                                    # 获取任务ID
                                    generate_id = result.get('data', {}).get('taskId')
                                    generate_result["generate_id"] = generate_id
                                    
                                    logging.info(f"RunningHub hd_resolution task submitted successfully, generate_id: {generate_id}")
                                                            
                                    #check generate result
                                    check_result = await self.check_generate_status(used_type, generate_id,extra_info)
                                    check_code = check_result["code"]
                                    check_message = check_result["msg"]
                                                                
                                    if check_code == 0: #成功
                                        generate_result["code"] = 0                            
                                        generate_result["image_url"] = check_result["image_url"]
                                        return generate_result
                                    else:                                    
                                        generate_result["code"] = check_code
                                        generate_result["msg"] = check_message
                                        return generate_result
                                                        
                except Exception as e:
                    # 其他异常
                    warning_msg = f"Submit hd_resolution request warning: {str(e)}"
                    logging.warning(warning_msg)
                    
                if attempt == self.max_retries - 1:  # 最后一次重试
                    error_msg = f"Submit hd_resolution request failed after {self.max_retries} attempts"
                    generate_result["code"] = 5
                    generate_result["msg"] = error_msg
                    logging.error(error_msg)
                    return generate_result
                else:
                    logging.warning(f"Submit hd_resolution attempt {attempt + 1}, retrying...")
                    await asyncio.sleep(2 ** attempt)  # 指数退避
                                
        except Exception as e:
            error_msg = f"Generate hd_resolution image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg, exc_info=True)
            return generate_result
        
        finally:
            # 确保在方法完全返回时释放并发槽位
            await self._release_request_slot(request_id)
                           
    
    async def check_generate_status(self, used_type, generate_id, extra_info):
        """
        查询图像生成状态和结果
        
        Args:
            used_type: 积分使用类型
            generate_id: 生成任务的ID
            
        Returns:
            dict: 包含状态和图像URL的字典
            
            {
                "code": check_code 
                "msg":"错误信息"
                "image_url":"图片url"
            }
            
            check_result code 的结果 -1 初始化的值 0 成功 1 进行中 2 积分不足 3 上传图片失败 4 任务失败 5 查询异常 6 解析图片失败 7 提示词或者图片非法
            
        需要完成图片上传和积分扣除的逻辑
        """
        
        #返回结果
        check_result = {
            "code" : -1,
            "msg" : "check status unknown",
            "image_url" : ""
        }
        
        url = f"https://{self.api_endpoint}/task/openapi/outputs"  # 根据实际API端点调整
        
        payload = {
            "apiKey": self.api_key,
            "taskId": generate_id
        }
        
        #检查结束时间
        end_time = time.time() + self.check_timeout
        
        logging.debug(f"Start to Check {generate_id} status")
        
        while True:                
            try:       
                async with aiohttp.ClientSession(timeout=self.timeout) as session:
                    async with session.post(url=url, headers=self.headers, json=payload) as status_response:
                        if status_response.status != 200:  
                            # 获取详细错误信息
                            try:
                                warning_detail = await status_response.text()
                                warning_msg = f"Check {generate_id} status failed: HTTP {status_response.status}, Detail: {warning_detail}"
                            except:
                                warning_msg = f"Check {generate_id} status failed: HTTP {status_response.status}"
                                                            
                            logging.warning(warning_msg)
                            
                        else:  
                            status_result = await status_response.json()
                            
                            # logging.info(f"Check RunningHub task {generate_id} success, status_result: {status_result}")
                            
                            status_code = status_result.get('code')
                                                
                            # 根据实际API响应格式调整
                            if status_code == 0:
                                task_data = status_result.get('data', [])
                                
                                # logging.info(f"Check RunningHub task {generate_id} success, task_data: {task_data}")
                                
                                if task_data:
                                    task_result = task_data[0]
                                    
                                    task_cost_time = task_result.get('taskCostTime', 2)
                                    # 一秒 0.2RH币  0.36分一个RH币(不打折) 独占机器是0.057分。汇率按照7算
                                    task_credits = float(task_cost_time) * 0.2 * 0.36 / 7.0 # 对应的美分
                                    
                                    extra_credits = extra_info.get("extra_credits", 0)
                                    credits_cost = task_credits + extra_credits
                                
                                    # 获取生成的图片URL
                                    image_url = task_result.get('fileUrl', '')
                                    
                                    need_parse_url = extra_info.get("need_parse_url", False)
                                    
                                    if need_parse_url:
                                        # 如果 image_url 是远程 txt 文件，需要读取其内容
                                        for attempt in range(self.max_retries):
                                            try:
                                                txt_response = requests.get(image_url, timeout=10)
                                                if txt_response.status_code == 200:
                                                    # 读取 txt 文件内容
                                                    txt_content = txt_response.text
                                                    # 假设 txt 文件内容是真正的图片 URL
                                                    image_url = txt_content.strip()
                                                    break
                                                else:
                                                    warning_msg = f"Task {generate_id} failed to read txt file: HTTP {txt_response.status_code}"
                                                    logging.warning(warning_msg)

                                            except Exception as e:
                                                warning_msg = f"Task {generate_id} failed to read txt file: {str(e)}"
                                                logging.warning(warning_msg)
                                                                                            
                                            if attempt == self.max_retries - 1:  # 最后一次重试
                                                error_msg = f"Parse image url task failed after {self.max_retries} attempts"
                                                logging.error(error_msg)
                                                check_result["code"] = 6
                                                check_result["msg"] = error_msg
                                                return check_result
                                            else:
                                                logging.warning(f"Parse image url task attempt {attempt + 1}, retrying...")
                                                await asyncio.sleep(2 ** attempt)  # 指数退避
                                        
                                    # logging.info(f"task result is {status_result}")
                                    
                                    #调用cloudflare上传图片
                                    cdn_instance = create_cdn_instance()
                                    upload_result = await cdn_instance.upload_from_url(image_url)
                                    
                                    if upload_result["status"] == "success":
                                        if await deduct_used_credits("runninghub", used_type, generate_id, credits_cost):
                                            check_result["code"] = 0
                                            check_result["image_url"] = upload_result["resource_url"]
                                            check_result["msg"] = "success"
                                            
                                        else:
                                            check_result["code"] = 2
                                            check_result["msg"] = "credits is not enough"
                                    else:
                                        check_result["code"] = 3
                                        check_result["msg"] = "upload failed"
                                    
                                    return check_result
                                
                                else:
                                    # 任务失败
                                    error_msg = f"Check RunningHub task {generate_id} status failed, result: {status_result}"
                                    logging.error(error_msg)
                                    check_result["code"] = 4
                                    check_result["msg"] = error_msg
                                    return check_result
                            # https://www.runninghub.cn/runninghub-api-doc/doc-6913922
                            elif status_code == 804 or status_code == 813:
                                # 任务仍在进行中
                                pass
                            else:
                                # 任务失败
                                error_data = status_result.get('data')
                                
                                # 处理多重转义的JSON
                                try:
                                    if isinstance(error_data, dict) and 'failedReason' in error_data:
                                        # 尝试解析failedReason
                                        failed_reason = error_data['failedReason']
                                        try:
                                            parsed_failed_reason = json.loads(failed_reason)
                                            error_data['failedReason'] = parsed_failed_reason
                                        except:
                                            pass
                                    
                                    # 格式化为可读JSON
                                    clean_error = json.dumps(error_data, ensure_ascii=False, indent=2)
                                    error_msg = f"Check RunningHub task {generate_id} status failed, result: {clean_error}"
                                except Exception:
                                    error_msg = f"Check RunningHub task {generate_id} status failed, result: {error_data}"
            
                                logging.error(error_msg)
                                check_result["code"] = 7
                                check_result["msg"] = error_msg
                                return check_result                
            except Exception as e:
                # 其他异常
                warning_msg = f"Check RunningHub task {generate_id} status exception: {str(e)}"
                logging.warning(warning_msg)
            
            #5分钟超时检查
            if time.time() > end_time:
                error_msg = f"Check status timeout, task {generate_id}"
                check_result["msg"] = error_msg
                check_result["code"] = 5
                logging.error(error_msg) 
                return check_result
            
            await asyncio.sleep(1)  # 添加1秒延迟，避免过于频繁的轮询
                    
image_runninghub_instance = ImageRunningHub()