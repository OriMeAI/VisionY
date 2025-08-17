from app.utils.core import get_user_id
from app.collections.user import is_user_has_credits, deduct_user_credits
import logging,math

async def check_for_credits() -> bool:
    user_id = get_user_id()
    if user_id:
        return await is_user_has_credits(user_id)
    return True

async def deduct_used_credits(used_channel, used_type, used_token, used_credits) -> bool:
    user_id = get_user_id()
    if user_id:
        #根据不同的used_channel 计算对应的扣点
        if used_channel == "liblib":
            modified_used_credits = used_credits * 1.2
        elif used_channel == "runninghub":
            modified_used_credits = used_credits * 1.2
        elif used_channel == "openAI":
            modified_used_credits = used_credits * 1.2
        elif used_channel == "Gemini":
            modified_used_credits = used_credits * 1.2
        elif used_channel == "comfyicu":
            modified_used_credits = used_credits * 1.2
        elif used_channel == "openrouter": 
            modified_used_credits = used_credits * 1.2
        else:
            modified_used_credits = used_credits * 1.2
            
        real_used_credits = math.ceil(modified_used_credits)
        
        deduct_result = await deduct_user_credits(used_channel, user_id, used_type, used_token, real_used_credits)
        
        logging.info(f"deduct_used_credits, user_id: {user_id},used_channel: {used_channel}, used_type: {used_type}, used_token: {used_token}, used_credits: {used_credits}, modified_used_credits: {modified_used_credits}, real_used_credits: {real_used_credits}, deduct_result: {deduct_result}")
        
        return deduct_result
    return True
