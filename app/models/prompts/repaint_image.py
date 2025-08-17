"""
包含 重绘图像的提示词

"""

def get_repaint_prompt_with_no_mask(image_prompt):
    """
    获取重绘图像的提示词

    Args:
        image_prompt: 图像生成提示词
    Returns:
        str: 重绘图像的提示词
    """
    # 全图重绘（无蒙版）
    image_prompt = image_prompt + ". Keep the artistic style of the image and other content unchanged. Maintain original composition and visual consistency."
    return image_prompt
        
def get_repaint_prompt_with_mask(image_prompt):
    """
    获取重绘图像的提示词

    Args:
        image_prompt: 图像生成提示词
    Returns:
        str: 重绘图像的提示词
    """

    # 局部重绘（有蒙版）- 简化版本
    image_prompt = f"Modify the red masked area: {image_prompt}. Remove all red mask completely. Keep the artistic style of the image and other content unchanged. Maintain original composition and visual consistency."
    return image_prompt