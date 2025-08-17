import aiohttp
import asyncio
import json
import logging
import os
import time
from app.collections.credits_helper import check_for_credits,deduct_used_credits
from app.utils.helper import generate_random_string

"""
https://openrouter.ai/

model:
google/gemini-2.5-flash
google/gemini-2.5-pro
openai/gpt-5
deepseek/deepseek-chat-v3-0324:free
deepseek/deepseek-chat-v3-0324
anthropic/claude-sonnet-4
x-ai/grok-3
z-ai/glm-4.5

  "reasoning": {
    // One of the following (not both):
    "effort": "high", // Can be "high", "medium", or "low" (OpenAI-style)
    "max_tokens": 2000, // Specific token limit (Anthropic-style)
    // Optional: Default is false. All models support this.
    "exclude": false, // Set to true to exclude reasoning tokens from response
    // Or enable reasoning with the default parameters:
    "enabled": true // Default: inferred from `effort` or `max_tokens`
  }

"""

class LLMOpenRouter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        OpenRouterLLM客户端
        
        Args:
            model: 模型名称，
            比如 "google/gemini-2.5-flash"、 "anthropic/claude-sonnet-4"
            参照上面的模型参数
        """
        
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        
        self.api_key = os.environ.get("OPENROUTER_API_KEY", "")
        
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            'Content-Type': 'application/json',
            'HTTP-Referer': 'https://www.visiony.ai', # Optional. Site URL for rankings on openrouter.ai.
            'X-Title': 'VisionY',  # Optional. Site title for rankings on openrouter.ai.
        }
        self.model = "anthropic/claude-sonnet-4"
        
        # 必须推理的模型
        self.reasoning_models = ["openai/gpt-5","google/gemini-2.5-pro"]
        
        #重试次数
        self.max_retries = 3
        
        # 添加超时配置
        # self.timeout = aiohttp.ClientTimeout(
        #     total=60,      # 总超时时间60秒
        #     connect=10,    # 连接超时10秒
        #     sock_read=30   # 读取超时30秒
        # )
        
        logging.info(f"Initialized OpenRouter LLMModel, LLM Model is: {self.model}")
              
    async def generate_content(self, messages, temperature = 1.0, is_json=False, used_type = "parse_script"):
        """
        异步标准生成
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            is_json: 是否返回json格式

        Returns:
            str: 生成的文本内容
        """            
        # 构建 API 调用参数
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            # 设置模型最大输出长度为 64*1024 token，实际为 input+output
            "max_tokens": 64 * 1024,
            # 控制生成文本的多样性，值越高，生成文本的多样性越强，取值范围为0-2，默认为1
            # 根据https://api-docs.deepseek.com/zh-cn/quick_start/parameter_settings 设置
            "temperature":temperature, #1.5 是deepseek官方建议的文学书写的值，比较有想象力。但是对于镜头拆分1.0即可
            #推理模型的设置
            "reasoning": {
                "enabled": False # Default: inferred from `effort` or `max_tokens`
            },
            "usage": {
                "include": True
            }   
        }
        
        if is_json:
            payload["response_format"] = {
                "type": "json_object"
            }
            
        if self.model in self.reasoning_models:            
            payload["reasoning"]["enabled"] = True
            payload["reasoning"]["max_tokens"] = 1000
            payload["reasoning"]["exclude"] = False
            
        # 开始计时
        start_time = time.time()
            
        for attempt in range(self.max_retries):
            try:                
                async with aiohttp.ClientSession() as session:
                    async with session.post(self.base_url, headers=self.headers, json=payload) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            logging.error(f"LLMOpenRouter API error {response.status}: {error_text}")
                        
                        else:     
                            # 非流式响应
                            completion = await response.json()
                            
                            # logging.info(f"LLMOpenRouter API response: {completion}")
                            
                            if completion and "choices" in completion and completion["choices"]:
                                usage_stats = completion["usage"]
                                usage_cost = usage_stats['cost']
                                
                                # TODO 是否需要检测用户的积分额度？
                                credits_cost = usage_cost * 100
                                
                                used_token = generate_random_string()
                                
                                # 计算耗时
                                end_time = time.time()
                                duration = end_time - start_time

                                logging.info(f"LLMOpenRouter API stream response: usage_stats is {usage_stats}, used_token is {used_token}, usage_cost is {usage_cost}, credits_cost is {credits_cost}, duration is {duration:.2f}")

                                # TODO 临时禁用LLM扣积分
                                await deduct_used_credits("openrouter", used_type, used_token, credits_cost)

                                return completion["choices"][0]["message"]["content"]
                        
            except Exception as e:
                logging.error(f"LLMOpenRouter generate_content error: {e}")
                # return None
                        
            # except (aiohttp.ServerTimeoutError, asyncio.TimeoutError) as e:
            if attempt == self.max_retries - 1:  # 最后一次重试
                logging.error(f"LLMOpenRouter generate_content Final timeout attempt after {self.max_retries} attempts")
                return None
            else:
                logging.warning(f"LLMOpenRouter generate_content attempt {attempt + 1} for task , retrying...")
                await asyncio.sleep(2 ** attempt)  # 指数退避
                            
    async def generate_stream(self, messages, temperature=1.0, is_json=False, used_type = "expand_write"):
        """
        异步流式生成 - 修复UTF-8解码问题
        
        Args:
            messages: 台词消息列表
            temperature: 温度参数
            
        Yields:
            str: 实时生成的文本块
        """
        # 构建 API 调用参数
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": True,
            "max_tokens": 64 * 1024,
            "temperature": temperature,
            "reasoning": {
                "enabled": False
            },
            "usage": {
                "include": True
            }   
        }
        
        if is_json:
            payload["response_format"] = {
                "type": "json_object"
            }
            
        if self.model in self.reasoning_models:
            payload["reasoning"]["enabled"] = True
            payload["reasoning"]["max_tokens"] = 1000
            payload["reasoning"]["exclude"] = False
        
        # 重置不完整字节缓冲区
        incomplete_bytes = b''
        
        for attempt in range(self.max_retries):
            try:                
                async with aiohttp.ClientSession() as session:
                    async with session.post(self.base_url, headers=self.headers, json=payload) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            logging.error(f"OpenRouter API error {response.status}: {error_text}")
                            
                        else:
                            buffer = ""
                            async for chunk in response.content.iter_chunked(1024):
                                # 处理UTF-8解码问题
                                try:
                                    # 将新数据与之前不完整的字节合并
                                    combined_bytes = incomplete_bytes + chunk
                                    
                                    # 尝试解码
                                    decoded_text = combined_bytes.decode('utf-8')
                                    incomplete_bytes = b''  # 清空缓冲区
                                    buffer += decoded_text
                                    
                                except UnicodeDecodeError as e:
                                    # 处理不完整的UTF-8字符
                                    if e.start > 0:
                                        # 部分数据可以解码
                                        valid_bytes = combined_bytes[:e.start]
                                        incomplete_bytes = combined_bytes[e.start:]
                                        buffer += valid_bytes.decode('utf-8')
                                    else:
                                        # 整个chunk都是不完整的，保存起来等待下一个chunk
                                        incomplete_bytes = combined_bytes
                                        continue
                                
                                # 处理SSE数据流
                                while '\n' in buffer:
                                    line, buffer = buffer.split('\n', 1)
                                    line = line.strip()
                                    
                                    if line.startswith('data: '):
                                        data = line[6:]  # 移除 'data: ' 前缀
                                        if data == '[DONE]':
                                            return
                                        try:
                                            chunk_data = json.loads(data)
                                            
                                            # 检查是否包含 usage 信息
                                            if 'usage' in chunk_data and chunk_data['usage']:
                                                usage_stats = chunk_data['usage']
                                                usage_cost = usage_stats.get('cost', 0)
                                                
                                                # TODO 是否需要检测用户的积分额度？
                                                credits_cost = usage_cost * 100
                                                
                                                used_token = generate_random_string()
                                                # TODO 临时禁用LLM扣积分
                                                await deduct_used_credits("openrouter", used_type, used_token, credits_cost)
                                                logging.info(f"LLMOpenRouter API stream response: usage_stats is {usage_stats}, used_token is {used_token}, usage_cost is {usage_cost}, credits_cost is {credits_cost}")
                                                
                                            if 'choices' in chunk_data and chunk_data['choices']:
                                                choice = chunk_data['choices'][0]
                                                if 'delta' in choice and 'content' in choice['delta']:
                                                    content = choice['delta']['content']
                                                    if content:
                                                        yield content
                                        except json.JSONDecodeError as json_err:
                                            logging.warning(f"JSON decode error: {json_err}, data: {data}")
                                            continue
                                    else:
                                        # 发送heartbeat保持连接
                                        if line:  # 只有非空行才发送heartbeat
                                            yield "\n"
                            
                            # 处理最后剩余的不完整字节
                            if incomplete_bytes:
                                try:
                                    final_text = incomplete_bytes.decode('utf-8', errors='ignore')
                                    if final_text.strip():
                                        buffer += final_text
                                        # 处理最后的数据
                                        while '\n' in buffer:
                                            line, buffer = buffer.split('\n', 1)
                                            line = line.strip()
                                            if line.startswith('data: '):
                                                data = line[6:]
                                                if data != '[DONE]':
                                                    try:
                                                        chunk_data = json.loads(data)
                                                        
                                                        # 检查是否包含 usage 信息
                                                        if 'usage' in chunk_data and chunk_data['usage']:
                                                            usage_stats = chunk_data['usage']
                                                            usage_cost = usage_stats.get('cost', 0)
                                                            
                                                            # TODO 是否需要检测用户的积分额度？
                                                            credits_cost = usage_cost * 100
                                                            
                                                            used_token = generate_random_string()
                                                            # TODO 临时禁用LLM扣积分
                                                            await deduct_used_credits("openrouter", used_type, used_token, credits_cost)
                                                            logging.info(f"LLMOpenRouter API stream response: usage_stats is {usage_stats}, used_token is {used_token}, usage_cost is {usage_cost}, credits_cost is {credits_cost}")
                                                                                                        
                                                        if 'choices' in chunk_data and chunk_data['choices']:
                                                            choice = chunk_data['choices'][0]
                                                            if 'delta' in choice and 'content' in choice['delta']:
                                                                content = choice['delta']['content']
                                                                if content:
                                                                    yield content
                                                    except json.JSONDecodeError:
                                                        continue
                                except UnicodeDecodeError:
                                    logging.warning("Final incomplete bytes could not be decoded")
                                finally:
                                    incomplete_bytes = b''
                                                        
            except Exception as e:
                logging.error(f"LLMOpenRouter generate_stream error: {e}")
                # return None
                        
            # except (aiohttp.ServerTimeoutError, asyncio.TimeoutError) as e:
            if attempt == self.max_retries - 1:  # 最后一次重试
                logging.error(f"LLMOpenRouter generate_stream Final timeout attempt after {self.max_retries} attempts")
                return
            else:
                logging.warning(f"LLMOpenRouter generate_stream attempt {attempt + 1} for task , retrying...")
                await asyncio.sleep(2 ** attempt)  # 指数退避
        
llm_openrouter_instance = LLMOpenRouter()

if __name__ == "__main__":
    import asyncio
    
    import sys
    import os
    
    # 添加项目根目录到 Python 路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.join(current_dir, '..', '..', '..')
    sys.path.insert(0, project_root)
    
    from init_env import initialize_environment_variables
    
    # 调用函数初始化环境变量
    initialize_environment_variables()
    
    llm = LLMOpenRouter()
    
    api_key = llm.api_key
    
    print(f"api_key is {api_key}")
    
    
    # 异步示例用法
    async def main():
        # 标准请求示例
        print("----- standard request -----")
        messages = [
            {"role": "system", "content": "你是人工智能助手."},
            {"role": "user", "content": "常见的十字花科植物有哪些？"},
        ]
        response = await llm.generate_content(messages)
        print(response)
        
        # 流式请求示例
        print("----- streaming request -----")
        async for content in llm.generate_stream(messages):
            print(content, end="")
        print()
    
    asyncio.run(main())