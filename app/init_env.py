import os
from pathlib import Path
from dotenv import load_dotenv

def initialize_environment_variables():
    """
    将配置文件中的内容设置到环境变量中
    """
    
    # 项目根目录配置
    PROJECT_ROOT: Path = Path(__file__).parent
    LOGS_DIR: Path = PROJECT_ROOT / 'logs'
    os.environ["PROJECT_ROOT"] = str(PROJECT_ROOT)
    os.environ["LOGS_DIR"] = str(LOGS_DIR)
    
    os.environ["SESSION_SECRET_KEY"] = "8DlkkT_bsYPZWDUwQLpm76Oh7I0bHIIMG48P8W_pkWA"
    
    # 语言模型配置
    os.environ["LLM_MODEL_NAME"] = "openrouter"
    
    # 图片生成配置 liblib runninghub
    os.environ["IMAGE_MODEL_NAME"] = "runninghub"
    
    # 加载 .env 文件 中的其他环境变量
    load_dotenv()
    
    # print("Init env variables successfully")

