import hmac,asyncio
import os
import logging
import aiohttp
from datetime import datetime
import hashlib
import uuid
import base64

from app.utils.core import get_language
from app.models.model_factory import create_cdn_instance
from app.collections.credits_helper import check_for_credits,deduct_used_credits
from .image_base.image_base import ImageBase

"""
文档地址
https://liblibai.feishu.cn/wiki/UAMVw67NcifQHukf8fpccgS5n6d
"""

from .liblib_api import flux_dev_generate_character_with_lora
from .liblib_api import kontext_dev_with_characters
from .liblib_api import kontext_dev_no_characters
from .liblib_api import kontext_dev_mask_edit
from .liblib_api import kontext_dev_text_edit
from .liblib_api import kontext_dev_simple_hd

from .liblib_api import kontext_pro_no_characters
from .liblib_api import kontext_pro_with_characters

default_role_blank_url = "https://resource-visual-story.unit-cdn.net/image/opaque_white_576_1024.png"

class ImageLibLib(ImageBase):
    """
    liblib AI 图像生成模型实现
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
        self.model_name = "liblib"
        # 从环境变量获取密钥
        # 从环境变量获取密钥
        self.access_key = os.environ.get("XINGLIU_ACCESS_KEY", "")
        self.secret_key = os.environ.get("XINGLIU_SECRET_KEY", "")
        self.headers = {'Content-Type': 'application/json'}
        logging.info(f"Initialized LibLibComfy ImageModel")
        
    def _generate_parameters(self, url:str) -> str:
        """
        生成调用接口的参数
        """
        time_stamp = int(datetime.now().timestamp() * 1000)
        signature_nonce = uuid.uuid1()
        
        # Calculate signature for ultra endpoint
        data_to_sign_ultra = url + "&" + str(time_stamp) + "&" + str(signature_nonce)
        hmac_code_ultra = hmac.new(self.secret_key.encode(), data_to_sign_ultra.encode(), hashlib.sha1) # type: ignore
        signature = base64.urlsafe_b64encode(hmac_code_ultra.digest()).rstrip(b'=').decode()
        
        return f"https://openapi.liblibai.cloud{url}?AccessKey={self.access_key}&Signature={signature}&Timestamp={time_stamp}&SignatureNonce={signature_nonce}"
                    
    def get_model_name(self):
        """
        获取模型名称

        Returns:
            模型名称
        """
        return self.model_name
                          
    async def generate_character_image(self, used_type,prompt, style_type=1, size="576x1024", n=1, seed=1234):
        """
        生成角色立绘图像
        
        Args:
            prompt: 图像生成提示词
            style_type: 风格类型ID
            size: 图像尺寸，格式为"宽x高"
            n: 生成图像数量
            seed: 随机种子
            
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
                
        # 解析尺寸
        if "x" in size:
            width, height = map(int, size.split("x"))
        else:
            # Default size if not specified correctly
            width, height = 576, 1024 
                                
        image_style,image_prompt = self.get_character_style_prompt(style_type,prompt)
        generate_result["image_prompt"] = image_prompt
        
        workflow_parameter = flux_dev_generate_character_with_lora.get_workflow_api(seed,image_style, width, height,prompt)
             
        try:            
            # 构建API URL
            url = self._generate_parameters("/api/generate/comfyui/app")
            
            # 提交任务
            logging.info(f"Submitting task to LibLibComfy: {url}")
                                                
            # 修改payload格式，包含workflow_id和prompt, files
            payload = workflow_parameter
                                    
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=self.headers, json=payload) as response:
                    if response.status != 200:
                        # 获取详细错误信息
                        try:
                            error_detail = await response.text()
                            error_msg = f"Commit LibLibComfy task failed: HTTP {response.status}, Detail: {error_detail}"
                        except:
                            error_msg = f"Commit LibLibComfy task failed: HTTP {response.status}"
                        
                        logging.error(error_msg)
                        
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        return generate_result
                    
                    result = await response.json()
                    
                    if result.get('code') == 0:
                        generate_id = result['data']['generateUuid']                                                                    
                        # 如果获取到任务ID
                        generate_result["generate_id"] = generate_id
                        
                        logging.info(f"LibLibComfy Task submitted successfully, generate_id: {generate_id}")
                        
                        #check generate result
                        while True:
                            check_result = await self.check_generate_status(used_type, generate_id)
                            check_code = check_result["code"]
                            check_message = check_result["msg"]
                                                        
                            if check_code == 0: #成功
                                generate_result["code"] = 0                            
                                generate_result["image_url"] = check_result["image_url"]
                                
                                return generate_result
                            elif check_code == 1: #处理中
                                await asyncio.sleep(1)  # 添加2秒延迟，避免过于频繁的轮询
                                continue
                            else:                                    
                                generate_result["code"] = check_code
                                generate_result["msg"] = check_message
                                                
                                return generate_result
                    else:
                        # 任务提交失败
                        error_msg = f'LibLibComfy task submission error, result: {result}'
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        logging.error(error_msg)
                        return generate_result
                
        except aiohttp.ClientError as e:
            # 请求异常
            error_msg = f"HTTP request error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
        except Exception as e:
            # 其他异常
            error_msg = f"Generate image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
               
    #专门绘制分镜的接口
    async def generate_shot_image_with_characters(self,used_type,prompt,style_type,size, seed,first_character,second_character,third_character):
        """
        绘制分镜
        
        Args:
            seed: 随机种子
            width: 图像宽度
            height: 图像高度
            image_prompt: 图像生成提示词
            first_character: 第一个角色
            second_character: 第二个角色
            third_character: 第三个角色
            
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
        
        # -1 默认值 0 代表成功 1 代表失败 2 代表用户积分不足
        generate_result = {"code":-1, "generate_id":"","image_prompt":"" ,"msg":"something is wrong"}
        
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
            
        #解析 aspect_ratio            
        aspect_ratio = self.get_aspect_ratio(size)
                                
        image_style,image_prompt = self.get_shot_style_prompt(style_type,prompt,empty_scene)
        generate_result["image_prompt"] = image_prompt
        
        if empty_scene:
            workflow_parameter = kontext_pro_no_characters.get_workflow_api(seed,aspect_ratio,image_prompt)
        else:
            workflow_parameter = kontext_pro_with_characters.get_workflow_api(seed,aspect_ratio,image_prompt, first_character,second_character,third_character)
                             
        try:            
            # 构建API URL
            url = self._generate_parameters("/api/generate/comfyui/app")
            
            # 提交任务
            logging.info(f"Submitting task to LibLibComfy: {url}")
                                                
            # 修改payload格式，包含workflow_id和prompt, files
            payload = workflow_parameter
                                    
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=self.headers, json=payload) as response:
                    if response.status != 200:
                        # 获取详细错误信息
                        try:
                            error_detail = await response.text()
                            error_msg = f"Commit LibLibComfy task failed: HTTP {response.status}, Detail: {error_detail}"
                        except:
                            error_msg = f"Commit LibLibComfy task failed: HTTP {response.status}"
                        
                        logging.error(error_msg)
                        
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        return generate_result
                    
                    result = await response.json()
                    
                    if result.get('code') == 0:
                        generate_id = result['data']['generateUuid']                                                                    
                        # 如果获取到任务ID
                        generate_result["generate_id"] = generate_id
                        
                        logging.info(f"LibLibComfy Task submitted successfully, generate_id: {generate_id}")
                        
                        #check generate result
                        while True:
                            check_result = await self.check_generate_status(used_type, generate_id)
                            check_code = check_result["code"]
                            check_message = check_result["msg"]
                                                        
                            if check_code == 0: #成功
                                generate_result["code"] = 0                            
                                generate_result["image_url"] = check_result["image_url"]
                                
                                return generate_result
                            elif check_code == 1: #处理中
                                await asyncio.sleep(1)  # 添加2秒延迟，避免过于频繁的轮询
                                continue
                            else:                                    
                                generate_result["code"] = check_code
                                generate_result["msg"] = check_message
                                                
                                return generate_result
                    else:
                        # 任务提交失败
                        error_msg = f'LibLibComfy task submission error, result: {result}'
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        logging.error(error_msg)
                        return generate_result
                
        except aiohttp.ClientError as e:
            # 请求异常
            error_msg = f"HTTP request error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
        except Exception as e:
            # 其他异常
            error_msg = f"Generate image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
    
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
        
        # 根据style_type从LibLibStyleList获取相关参数
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
        
        logging.info(f"generate_repaint_image, image_prompt is {image_prompt}")
        
        # mask_data = None
                
        if mask_data:
            #调用cloudflare上传图片
            cdn_instance = create_cdn_instance()
            upload_result = await cdn_instance.upload_base64(mask_data, "mask_data.png")
            if upload_result["status"] != "success":
                generate_result["code"] = 5
                generate_result["msg"] = "upload mask_data failed"
                return generate_result
            else:
                mask_image = upload_result["resource_url"]
                logging.info(f"Repaint mask data uploaded successfully, URL: {mask_image}")
                mask_image = self.get_cn_resource_url(mask_image)
                workflow_parameter = kontext_dev_mask_edit.get_workflow_api(seed, image_prompt,base_image,mask_image)
        else:                                               
            workflow_parameter = kontext_dev_text_edit.get_workflow_api(seed,image_prompt,base_image)
            
        generate_result["image_prompt"] = image_prompt
            
        try:            
            # 构建API URL
            url = self._generate_parameters("/api/generate/comfyui/app")
            
            # 提交任务
            logging.info(f"Submitting Repaint task to LibLibComfy: {url}")
                                                
            # 修改payload格式，包含workflow_id和prompt, files
            payload = workflow_parameter
                                    
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=self.headers, json=payload) as response:
                    if response.status != 200:
                        # 获取详细错误信息
                        try:
                            error_detail = await response.text()
                            error_msg = f"Commit LibLibComfy Repaint task failed: HTTP {response.status}, Detail: {error_detail}"
                        except:
                            error_msg = f"Commit LibLibComfy Repaint task failed: HTTP {response.status}"
                        
                        logging.error(error_msg)
                        
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        return generate_result
                    
                    result = await response.json()
                    
                    if result.get('code') == 0:
                        generate_id = result['data']['generateUuid']                                                                    
                        # 如果获取到任务ID
                        generate_result["generate_id"] = generate_id
                        
                        logging.info(f"LibLibComfy Repaint Task submitted successfully, generate_id: {generate_id}")
                        
                        #check generate result
                        while True:
                            check_result = await self.check_generate_status(used_type, generate_id)
                            check_code = check_result["code"]
                            check_message = check_result["msg"]
                                                        
                            if check_code == 0: #成功
                                generate_result["code"] = 0                            
                                generate_result["image_url"] = check_result["image_url"]
                                
                                return generate_result
                            elif check_code == 1: #处理中
                                await asyncio.sleep(1)  # 添加2秒延迟，避免过于频繁的轮询
                                continue
                            else:                                    
                                generate_result["code"] = check_code
                                generate_result["msg"] = check_message
                                                
                                return generate_result
                    else:
                        # 任务提交失败
                        error_msg = f'LibLibComfy Repaint task submission error, result: {result}'
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        logging.error(error_msg)
                        return generate_result
                
        except aiohttp.ClientError as e:
            # 请求异常
            error_msg = f"HTTP Repaint request error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
        except Exception as e:
            # 其他异常
            error_msg = f"Generate Repaint image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
    
    #两倍细节放大
    async def hd_resolution(self,used_type,seed, style_type, prompt, image_url):
        """
        2倍高清放大

        Args:
            image_url: 原始图像URL
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
        
        image_url = self.get_cn_resource_url(image_url)
        
        # 根据style_type从LibLibStyleList获取相关参数
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

        logging.info(f"generate_hd_resolution_image, image_prompt is {image_prompt}")
                                                                    
        workflow_parameter = kontext_dev_simple_hd.get_workflow_api(seed,image_prompt,image_url)
             
        try:            
            # 构建API URL
            url = self._generate_parameters("/api/generate/comfyui/app")
            
            # 提交任务
            logging.info(f"Submitting HD task to LibLibComfy: {url}")
                                                
            # 修改payload格式，包含workflow_id和prompt, files
            payload = workflow_parameter
                                    
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=self.headers, json=payload) as response:
                    if response.status != 200:
                        # 获取详细错误信息
                        try:
                            error_detail = await response.text()
                            error_msg = f"Commit LibLibComfy HD task failed: HTTP {response.status}, Detail: {error_detail}"
                        except:
                            error_msg = f"Commit LibLibComfy HD task failed: HTTP {response.status}"
                        
                        logging.error(error_msg)
                        
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        return generate_result
                    
                    result = await response.json()
                    
                    if result.get('code') == 0:
                        generate_id = result['data']['generateUuid']                                                                    
                        # 如果获取到任务ID
                        generate_result["generate_id"] = generate_id
                        
                        logging.info(f"LibLibComfy HD Task submitted successfully, generate_id: {generate_id}")
                        
                        #check generate result
                        while True:
                            check_result = await self.check_generate_status(used_type, generate_id)
                            check_code = check_result["code"]
                            check_message = check_result["msg"]
                                                        
                            if check_code == 0: #成功
                                generate_result["code"] = 0                            
                                generate_result["image_url"] = check_result["image_url"]
                                
                                return generate_result
                            elif check_code == 1: #处理中
                                await asyncio.sleep(1)  # 添加2秒延迟，避免过于频繁的轮询
                                continue
                            else:                                    
                                generate_result["code"] = check_code
                                generate_result["msg"] = check_message
                                                
                                return generate_result
                    else:
                        # 任务提交失败
                        error_msg = f'LibLibComfy HD task submission error, result: {result}'
                        generate_result["code"] = 1
                        generate_result["msg"] = error_msg
                        logging.error(error_msg)
                        return generate_result
                
        except aiohttp.ClientError as e:
            # 请求异常
            error_msg = f"HTTP HD request error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
        except Exception as e:
            # 其他异常
            error_msg = f"Generate HD image error: {str(e)}"
            generate_result["code"] = 1
            generate_result["msg"] = error_msg
            logging.error(error_msg,exc_info=True)
            return generate_result
    

    async def check_generate_status(self, used_type, generate_id):
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
            
            check_result code 的结果 -1 初始化的值 0 成功 1 进行中 2 积分不足 3 上传图片失败 4 任务失败 5 查询异常
            
        需要完成图片上传和积分扣除的逻辑
        """
        # Construct URL for status endpoint
        url = self._generate_parameters("/api/generate/comfy/status") 
        
        status_data = {"generateUuid": generate_id}
        
        #返回结果
        check_result = {
            "code" : -1,
            "msg" : "check status unknown",
            "image_url" : ""
        }
        
        try:
            # 查询任务状态
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, headers=self.headers, json=status_data) as status_response:
                    if status_response.status != 200:              
                        # 获取详细错误信息
                        try:
                            error_detail = await status_response.text()
                            error_msg = f"Check LibLibComfy status failed: HTTP {status_response.status}, Detail: {error_detail}"
                        except:
                            error_msg = f"Check LibLibComfy status failed: HTTP {status_response.status}"
                                                        
                        logging.error(error_msg)
                        
                        check_result["code"] = 5
                        check_result["msg"] = error_msg
                        return check_result
                    
                    status_result = await status_response.json()
                    
                    if status_result.get('code') == 0:
                        # logging.info(f"Liblib Check status success, status_result: {status_result}")
                        # 检查是否有图像
                        if status_result['data'].get('images') and any(image for image in status_result['data']['images'] if image is not None):
                            # 任务已完成，返回第一张有效图像
                            for image in status_result['data']['images']:
                                if image:
                                    image_url = image["imageUrl"]
                                    
                                    progress_data = status_result['data']
                                    points_cost = progress_data["pointsCost"]
                                    account_balance = progress_data["accountBalance"]
                                    
                                    credits_cost = float(points_cost)/7.0
                                    
                                    if account_balance <= 0:
                                        logging.error(f"account_balance is not enough, account_balance: {account_balance}")
                                        # TODO need to send email to administrator
                                    
                                    #调用cloudflare上传图片
                                    cdn_instance = create_cdn_instance()
                                    upload_result = await cdn_instance.upload_from_url(image_url)
                                    
                                    if upload_result["status"] == "success":
                                        if await deduct_used_credits("liblib", used_type, generate_id,credits_cost):
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
                        
                        # 任务仍在进行中
                        check_result["code"] = 1
                        check_result["msg"] = "Image is processing, please wait."
                        return check_result
                    else:
                        # 任务失败
                        error_msg = f"Task failed: code {status_result.get('code')}, msg: {status_result.get('msg', 'Unknown error')}"
                        logging.error(error_msg)
                        check_result["code"] = 4
                        check_result["msg"] = error_msg
                        return check_result
                
        except aiohttp.ClientError as e:
            # 查询异常
            error_msg = f"Check LibLibComfy status failed: {str(e)}"
            logging.error(error_msg,exc_info=True)
            check_result["code"] = 5
            check_result["msg"] = error_msg
            return check_result

        except Exception as e:
            # 其他异常
            error_msg = f"Check LibLibComfy status exception: {str(e)}"
            logging.error(error_msg,exc_info=True)
            check_result["code"] = 5
            check_result["msg"] = error_msg
            return check_result
                    
image_liblib_instance = ImageLibLib()