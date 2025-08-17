import json
import logging
import os
from typing import List, Dict, Any, Union
import asyncio
import time

from volcengine.ApiInfo import ApiInfo
from volcengine.Credentials import Credentials
from volcengine.ServiceInfo import ServiceInfo
from volcengine.base.Service import Service

"""
API 说明地址：
https://www.volcengine.com/docs/4640/65067
"""

class TranslatorVolcengine:
    # _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance
    
    def __init__(self):
        """
        初始化火山引擎翻译器
        """
        # 从环境变量获取认证信息
        self.access_key = os.environ.get("VOLCENGINE_ACCESS_KEY", "")
        self.secret_key = os.environ.get("VOLCENGINE_SECRET_KEY", "")
        
        # 设置服务信息
        self.service_info = ServiceInfo(
            'translate.volcengineapi.com',
            {'Content-Type': 'application/json'},
            Credentials(self.access_key, self.secret_key, 'translate', 'cn-north-1'),
            5,
            5
        )
        
        # 设置API查询参数
        self.query = {
            'Action': 'TranslateText',
            'Version': '2020-06-01'
        }
        
        # 设置API信息
        self.api_info = {
            'translate': ApiInfo('POST', '/', self.query, {}, {})
        }
        
        # 创建服务实例
        self.service = Service(self.service_info, self.api_info)
        
        #重试次数
        self.max_retries = 3

    async def translate(self, texts: Union[str, List[str]], target_lang: str = "en") -> Dict[str, Any]:
        """
        异步翻译文本
        
        Args:
            texts: 要翻译的文本或文本列表
            target_lang: 目标语言代码
            
        Returns:
            Dict: 翻译结果
        """
        if isinstance(texts, str):
            texts_list = [texts]
        else:
            texts_list = texts
            
        # 创建请求体
        body = {
            'TargetLanguage': target_lang,
            'TextList': texts_list
        }
        for attempt in range(self.max_retries):
            try:
                start_time = time.time()
                # 使用线程池执行异步操作
                response = await asyncio.to_thread(
                    self.service.json,
                    'translate',
                    {},
                    json.dumps(body)
                )
                
                # 解析响应
                response_data = json.loads(response)
                translate_list = response_data.get("TranslationList", [])
                
                if translate_list:
                    translate_result = translate_list[0]["Translation"] if isinstance(texts, str) else [item["Translation"] for item in translate_list]
                else:
                    translate_result = []
                    
                end_time = time.time()
                duration = end_time - start_time
                logging.debug(f"Translate success, duration: {duration:.2f} seconds")
                    
                return {
                    "code": 0,
                    "msg": "Translate success",
                    "data": translate_result
                }
            except Exception as e:
                logging.error(f"Translate process exception: {str(e)}")

            if attempt == self.max_retries - 1:  # 最后一次重试
                error_msg = f"Translate service failed after {self.max_retries} attempts"
                return {
                    "code": 500,
                    "msg": error_msg,
                    "data": None
                }
            else:
                logging.warning(f"Translate service attempt {attempt + 1}, retrying...")
                await asyncio.sleep(2 ** attempt)  # 指数退避

# 创建翻译器实例
# translator_volcengine_instance = TranslatorVolcengine()
    
if __name__ == "__main__":    
    # 设置环境变量
    import sys
    import os
    translator = TranslatorVolcengine()
    
    # 将项目根目录添加到Python路径
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
    from init_env import initialize_environment_variables
    initialize_environment_variables()
    # 翻译测试
    async def test_translate():
        text_to_translate = 'こんにちは世界'
        target_language = "en"  # 翻译为英语
        
        result = await translator.translate(text_to_translate, target_language)
        print(result)
    
    # 运行测试
    asyncio.run(test_translate())