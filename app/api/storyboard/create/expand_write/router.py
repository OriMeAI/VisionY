from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse,JSONResponse
import json, asyncio,logging
from typing import AsyncGenerator

from app.models.model_factory import create_llm_model
from app.models.prompts.expand_write import get_expand_write_prompt
from app.utils.core import encode_sse_data

expand_write_router = APIRouter()

async def generate_expand_content(text: str) -> AsyncGenerator[bytes, None]:
    try:
        llm_model = create_llm_model()
        
        # 1 让AI续写故事
        messages = [
            {"role": "system", "content": get_expand_write_prompt()},
            {"role": "user", "content": text},
            {"role": "assistant", "content": text},
        ]
        
        message = {"text": text}
        yield encode_sse_data(message)

        # 使用真实LLM流式接口
        async for chunk in llm_model.generate_stream(messages, temperature = 1.5, is_json=False, used_type = "expand_write"):
            if chunk and chunk.strip():  # 正常的文本内容
                # 将每个文本块包装为SSE格式
                message = {"text": chunk}
                yield encode_sse_data(message)
            elif chunk == "\n":  # 心跳数据
                # 发送心跳事件到前端
                yield encode_sse_data("", event="heartbeat")    
        # 结束标记
        yield encode_sse_data("Complete")
    except Exception as e:
        logging.error(f"Error in generate_expand_content: {e}",exc_info=True)
        yield encode_sse_data("Server error",event="error")

@expand_write_router.post('/expand_write')
async def operator(request: Request):    
    body = await request.body()
    data = json.loads(body.decode())
    text = data.get('text', '')
        
    return StreamingResponse(
        generate_expand_content(text=text),
        media_type='text/event-stream; charset=utf-8',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
        }
    )