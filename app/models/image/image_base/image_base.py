"""
图像API的基类

主要是一些常量和方法

"""

import logging

from app.utils.core import get_language
from .image_style import get_project_image_style_list
from .image_size import get_project_image_size_list

class ImageBase:
    
    #这样写可以被基类和子类用self调用
    #角色合并的时间用来填充空位
    default_role_blank_url = "https://resource.visiony.cc/image/opaque_white_576_1024.png"
    
    #场景图的默认图片
    default_shot_image_url = "https://resource.visiony.cc/image/regenerate_background.jpg"
    
    #图片风格列表
    image_style_list = get_project_image_style_list()
    
    #图片尺寸列表
    image_size_list = get_project_image_size_list()
    
    def __init__(self):
        pass
            
    def get_cn_resource_url(self,resource_url):
        return resource_url
    
    def get_default_role_blank_url(self):
        return self.default_role_blank_url
    
    #获取场景图的默认图片
    def get_default_shot_image_url(self):
        return self.default_shot_image_url
    
    #获取图片尺寸列表
    def get_image_size_list(self):
        return self.image_size_list
    
    #根据aspect_ratio获取图片尺寸
    def get_image_size_by_aspect_ratio(self,aspect_ratio):
        for item in self.image_size_list:
            if item.get("value") == aspect_ratio:
                return item.get("tip")
        return "1024x1024"
    
    #根据size获取aspect_ratio
    def get_aspect_ratio(self,size):
        #解析 aspect_ratio
        for item in self.image_size_list:
            if item.get("tip") == size:
                return item.get("value")
        return "16:9"
    
    def get_model_image_style(self, style_type):
        """
        根据风格ID，获取风格详细描述

        Returns:
            风格详细描述
        """
        # 根据style_type从IMAGE_STYLE_LIST获取相关参数
        image_style = None
        image_style_description = None

        for style in self.image_style_list:
            if style["type_id"] == style_type:
                image_style = style["image_style"]
                image_style_description = style["image_style_description"]
                break
        
        # 如果找不到对应的风格，使用默认值
        if image_style is None and image_style_description is None:
            logging.warning(f"Can not find style {style_type}, use default style")
            style = self.image_style_list[0]
            image_style = style["image_style"]
            image_style_description = style["image_style_description"]
            
        return f"{image_style}, {image_style_description}"
    
    def get_role_image_size(self):
        """
        获取角色图像尺寸
        Returns:
            角色图像尺寸
        """
        return "576x1024"
    
    def get_role_image_size_by_height_percentage(self, height_percentage):
        """
        根据高度百分比，获取角色图像尺寸
        Returns:
            角色图像尺寸
        """
        height = int(1024*height_percentage/100.0)
        return f"576x{height}"
    
    def get_style_list(self):
        """
        获取风格列表，根据当前语言返回对应的风格名称
        
        Returns:
            list: 风格列表，每个风格包含id、name和avatar
        """
        language = get_language()
                          
        style_list = []
        for style in self.image_style_list:
            # 获取当前语言的风格名称
            style_name = style["type_desc"].get(language, style["type_desc"]["en"])
            
            # 构建风格项
            style_item = {
                "id": style["type_id"],
                "type": style["type_id"],
                "name": style_name,
                "image_url": style["image_url"]
            }
            style_list.append(style_item)
            
        return style_list
    
    #提示词相关
    def get_character_style_prompt(self,style_type,image_prompt):
        """
        获取风格化的生成角色形象的提示词
        """
        # 根据style_type从image_style_list获取相关参数
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
            
        style_prompt = f"{image_style}, {image_prompt}"
        
        # logging.debug(f"generate_character_image, image_prompt is {style_prompt}")
                    
        return image_style,style_prompt
    
    def get_shot_style_prompt(self,style_type,image_prompt,empty_scene):
        """
        获取风格化的生成分镜图的提示词
        
        Character appearance MUST be consistent with reference images, height proportions MUST strictly follow reference image, no scaling of torso or legs, MUST maintain original height ratios, hair colors MUST match reference exactly, clothing colors MUST match reference exactly, prop colors MUST match reference exactly.
        
        """
        # 根据style_type从image_style_list获取相关参数
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
            
        style_prompt = f"{image_style}, {image_prompt}"
        
        if not empty_scene:
            style_prompt = f"""Based on the character appearance in the reference image and the following storyboard description, COMPLETELY REGENERATE a new storyboard frame. 
             Character expressions, body language, and positions in the new frame must be generated strictly according to the textual description: 
            {style_prompt}""" 
        
        # logging.debug(f"generate_shot_image_with_characters, image_prompt is {style_prompt}")
        
        return image_style,style_prompt
    
    