from typing import Union, Dict, Any
from app.utils.core import get_language
from app.locales.languages.cn import SERVER_CONTENT as cn_content
from app.locales.languages.en import SERVER_CONTENT as en_content
from app.locales.languages.ja import SERVER_CONTENT as ja_content
from app.locales.languages.tw import SERVER_CONTENT as tw_content

# 定义翻译字典，将语言代码映射到对应的翻译内容
translations = {
    "cn": cn_content,
    "en": en_content,
    "ja": ja_content,
    "tw": tw_content
}
        
def get_translation(key: str, default_language=None) -> Union[Dict[str, Any], str]:
    """获取当前请求的翻译对象
    
    Args:
        key: 翻译键名
        
    Returns:
        对应语言的翻译内容
    """
    
    if default_language:
        language = default_language
    else:
        language = get_language()
        
    # 如果请求的语言不存在，默认使用英文
    if language not in translations:
        language = "en"
    
    try:
        # 如果请求的键不存在，返回键名本身
        if key not in translations[language]:
            return key
    except:
        print(f"translation key {key} not found")
        # 如果请求的键不存在，返回键名本身
        return key
    
    return translations[language][key]

from app.locales.stories.cn import get_stories_list as get_cn_tories_list
from app.locales.stories.en import get_stories_list as get_en_tories_list
from app.locales.stories.ja import get_stories_list as get_ja_tories_list
from app.locales.stories.tw import get_stories_list as get_tw_tories_list

stories_list = {
    "cn": get_cn_tories_list,
    "en": get_en_tories_list,
    "ja": get_ja_tories_list,
    "tw": get_tw_tories_list
}

def get_stories_list(default_language=None):
    """
    根据当前语言，获取对应的故事列表
    """
    if default_language:
        language = default_language
    else:
        language = get_language()
        
    # 如果请求的语言不存在，默认使用英文
    if language not in stories_list:
        language = "en"
        
    return stories_list[language]()

from app.locales.email_content.cn import get_email_content as get_cn_email_content
from app.locales.email_content.en import get_email_content as get_en_email_content
from app.locales.email_content.ja import get_email_content as get_ja_email_content
from app.locales.email_content.tw import get_email_content as get_tw_email_content

email_content = {
    "cn": get_cn_email_content,
    "en": get_en_email_content,
    "ja": get_ja_email_content,
    "tw": get_tw_email_content
}

def get_email_content(sign_number, default_language=None):
    """
    根据当前语言，获取对应的邮件内容
    """
    if default_language:
        language = default_language
    else:
        language = get_language()
        
    # 如果请求的语言不存在，默认使用英文
    if language not in email_content:
        language = "en"
        
    return email_content[language](sign_number)

###故事模版
from app.locales.template.cn import get_project_template_item as get_cn_project_template_item
from app.locales.template.en import get_project_template_item as get_en_project_template_item
from app.locales.template.ja import get_project_template_item as get_ja_project_template_item
from app.locales.template.tw import get_project_template_item as get_tw_project_template_item

project_template_item = {
    "cn": get_cn_project_template_item,
    "en": get_en_project_template_item,
    "ja": get_ja_project_template_item,
    "tw": get_tw_project_template_item
}

def get_project_template_item(default_language=None):
    """
    根据当前语言，获取对应的故事模版
    """
    if default_language:
        language = default_language
    else:
        language = get_language()
        
    # 如果请求的语言不存在，默认使用英文
    if language not in project_template_item:
        language = "en"
        
    return project_template_item[language]()

from app.locales.template.cn import get_project_description_item as get_cn_project_description_item
from app.locales.template.en import get_project_description_item as get_en_project_description_item
from app.locales.template.ja import get_project_description_item as get_ja_project_description_item
from app.locales.template.tw import get_project_description_item as get_tw_project_description_item

project_description_item = {
    "cn": get_cn_project_description_item,
    "en": get_en_project_description_item,
    "ja": get_ja_project_description_item,
    "tw": get_tw_project_description_item
}

def get_project_description_item(template_id: str,default_language=None):
    """
    根据当前语言，获取对应的故事模版
    """
    if default_language:
        language = default_language
    else:
        language = get_language()
        
    # 如果请求的语言不存在，默认使用英文
    if language not in project_description_item:
        language = "en"
        
    return project_description_item[language](template_id)

from app.locales.template.cn import get_project_role_item as get_cn_project_role_item
from app.locales.template.en import get_project_role_item as get_en_project_role_item
from app.locales.template.ja import get_project_role_item as get_ja_project_role_item
from app.locales.template.tw import get_project_role_item as get_tw_project_role_item

project_role_item = {
    "cn": get_cn_project_role_item,
    "en": get_en_project_role_item,
    "ja": get_ja_project_role_item,
    "tw": get_tw_project_role_item
}

def get_project_role_item(template_id: str,default_language=None):
    """
    根据当前语言，获取对应的故事模版
    """
    if default_language:
        language = default_language
    else:
        language = get_language()
        
    # 如果请求的语言不存在，默认使用英文
    if language not in project_role_item:
        language = "en"
        
    return project_role_item[language](template_id)

from app.locales.template.cn import get_project_shot_item as get_cn_project_shot_item
from app.locales.template.en import get_project_shot_item as get_en_project_shot_item
from app.locales.template.ja import get_project_shot_item as get_ja_project_shot_item
from app.locales.template.tw import get_project_shot_item as get_tw_project_shot_item

project_shot_item = {
    "cn": get_cn_project_shot_item,
    "en": get_en_project_shot_item,
    "ja": get_ja_project_shot_item,
    "tw": get_tw_project_shot_item
}

def get_project_shot_item(template_id: str,default_language=None):
    """
    根据当前语言，获取对应的故事模版
    """
    if default_language:
        language = default_language
    else:
        language = get_language()
        
    # 如果请求的语言不存在，默认使用英文
    if language not in project_shot_item:
        language = "en"
        
    return project_shot_item[language](template_id)
    