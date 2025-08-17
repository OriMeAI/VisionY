import os,sys,logging,re,warnings
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from .core import is_running_in_docker

# 创建一个警告过滤器，将警告转为日志
class WarningToLogFilter(warnings.WarningMessage):
    def __init__(self):
        self.logger = logging.getLogger()
    
    def __call__(self, message, category, filename, lineno, file=None, line=None):
        self.logger.warning(
            f'Warning: {message}\nCategory: {category.__name__}\nFile: {filename}:{lineno}'
        )

class CustomTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.suffix = "%Y_%m_%d.log"
        self.extMatch = re.compile(r"^.*_\d{4}_\d{2}_\d{2}\.log$", re.ASCII)

    def namer(self, default_name):
        base_name, _, last_part = default_name.rpartition('.')
        return f"{base_name.replace('.log.', '_')}.{last_part}"
    
class RelativePathFormatter(logging.Formatter):
    def format(self, record):
        if hasattr(record, 'pathname'):
            record.pathname = record.pathname.replace(os.environ.get("PROJECT_ROOT", "") + '/', '')
        return super().format(record)

def register_log_handlers():
    try: 
        # 先清除所有已存在的处理器
        root_logger = logging.getLogger()
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
               
        # 确保各个日志目录存在
        logs_dir = Path(os.environ.get("LOGS_DIR", ""))
        log_dirs = {
            'app': logs_dir / 'app',
            'uvicorn_access': logs_dir / 'uvicorn/access',
            'uvicorn_error': logs_dir / 'uvicorn/error',
            'gunicorn_access': logs_dir / 'gunicorn/access',
            'gunicorn_error': logs_dir / 'gunicorn/error',
        }
        for dir_path in log_dirs.values():
            os.makedirs(dir_path, exist_ok=True)

        # 统一的日志格式
        formatter = RelativePathFormatter(
            '%(asctime)s - [%(process)d:%(thread)d] - %(name)s - %(levelname)s - %(pathname)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
                
        # 文件处理器
        file_handler = CustomTimedRotatingFileHandler(
            filename= os.path.join(log_dirs['app'], 'app.log'),
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        
        # 控制台处理器
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)

        # 设置根日志记录器
        root_logger = logging.getLogger()
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)
        
        if is_running_in_docker():
            root_logger.setLevel(logging.INFO)   
        else:
            root_logger.setLevel(logging.DEBUG)   
                    
        # 配置 uvicorn 日志
        uvicorn_logger = logging.getLogger('uvicorn')
        uvicorn_access_logger = logging.getLogger('uvicorn.access')
        uvicorn_error_logger = logging.getLogger('uvicorn.error')
        
        # 清理现有处理器
        for logger in [uvicorn_logger, uvicorn_access_logger, uvicorn_error_logger]:
            logger.handlers.clear()
            logger.propagate = False
           
        # 文件处理器
        uvicorn_file_handler = CustomTimedRotatingFileHandler(
            filename= os.path.join(log_dirs['uvicorn_access'], 'access.log'),
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf-8'
        )
        uvicorn_file_handler.setFormatter(formatter)
        uvicorn_file_handler.setLevel(logging.INFO)
        
        # 文件处理器
        uvicorn_error_file_handler = CustomTimedRotatingFileHandler(
            filename= os.path.join(log_dirs['uvicorn_error'], 'error.log'),
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf-8'
        )
        uvicorn_error_file_handler.setFormatter(formatter)
        uvicorn_error_file_handler.setLevel(logging.INFO)
        
        # 控制台处理器
        uvicorn_console_handler = logging.StreamHandler(sys.stdout)
        uvicorn_console_handler.setFormatter(formatter)
        uvicorn_console_handler.setLevel(logging.ERROR)
        
        uvicorn_logger.setLevel(logging.INFO)
        uvicorn_logger.addHandler(uvicorn_file_handler)
        uvicorn_logger.addHandler(uvicorn_console_handler)

        uvicorn_access_logger.setLevel(logging.INFO)
        uvicorn_access_logger.addHandler(uvicorn_file_handler)
        uvicorn_access_logger.addHandler(uvicorn_console_handler)
                        
        uvicorn_error_logger.setLevel(logging.INFO)
        uvicorn_error_logger.addHandler(uvicorn_error_file_handler)
        uvicorn_error_logger.addHandler(uvicorn_console_handler)
        
        # 配置 Gunicorn 日志
        gunicorn_logger = logging.getLogger('gunicorn')
        gunicorn_error_logger = logging.getLogger('gunicorn.error')
        gunicorn_access_logger = logging.getLogger('gunicorn.access')
                
        # 清理现有处理器
        for logger in [gunicorn_logger, gunicorn_access_logger, gunicorn_error_logger]:
            logger.handlers.clear()
            logger.propagate = False
            
        # 文件处理器
        gunicorn_file_handler = CustomTimedRotatingFileHandler(
            filename= os.path.join(log_dirs['gunicorn_access'], 'access.log'),
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf-8'
        )
        gunicorn_file_handler.setFormatter(formatter)
        gunicorn_file_handler.setLevel(logging.INFO)
        
        gunicorn_error_file_handler = CustomTimedRotatingFileHandler(
            filename= os.path.join(log_dirs['gunicorn_error'], 'error.log'),
            when='midnight',
            interval=1,
            backupCount=30,
            encoding='utf-8'
        )
        gunicorn_error_file_handler.setFormatter(formatter)
        gunicorn_error_file_handler.setLevel(logging.INFO)
        
        gunicorn_console_handler = logging.StreamHandler()
        gunicorn_console_handler.setFormatter(formatter)
        gunicorn_console_handler.setLevel(logging.ERROR)  # 只在控制台显示错误
        
        gunicorn_logger.addHandler(gunicorn_file_handler)
        gunicorn_logger.addHandler(gunicorn_console_handler)
        gunicorn_logger.setLevel(logging.INFO)
                
        gunicorn_access_logger.addHandler(gunicorn_file_handler)
        gunicorn_access_logger.addHandler(gunicorn_console_handler)
        gunicorn_access_logger.setLevel(logging.INFO)
        
        gunicorn_error_logger.addHandler(gunicorn_error_file_handler)
        gunicorn_error_logger.addHandler(gunicorn_console_handler)
        gunicorn_error_logger.setLevel(logging.INFO)
        
        #屏蔽mongo的日志输出
        logging.getLogger("pymongo").setLevel(logging.WARNING)
        
        #屏蔽httpcore和httpx的日志输出
        logging.getLogger("httpcore").setLevel(logging.WARNING)
        logging.getLogger("httpx").setLevel(logging.WARNING) 
        
        # 新增火山引擎SDK日志过滤
        logging.getLogger("volcenginesdkarkruntime").setLevel(logging.WARNING)
        
        #新增openai SDK的日志输出过滤
        logging.getLogger("openai").setLevel(logging.WARNING)
        
        # 屏蔽urllib3的日志输出
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        
        #屏蔽腾讯cos日志
        logging.getLogger("qcloud_cos.cos_auth").setLevel(logging.WARNING)
        logging.getLogger("qcloud_cos.cos_client").setLevel(logging.WARNING)
        
        #屏蔽stripe日志
        logging.getLogger("stripe").setLevel(logging.WARNING)
        
        #屏蔽aliyun oss日志
        logging.getLogger("oss2.auth").setLevel(logging.WARNING)
        logging.getLogger("oss2.http").setLevel(logging.WARNING)
        logging.getLogger("oss2.api").setLevel(logging.WARNING)
        
        # 添加警告处理
        warnings.showwarning = WarningToLogFilter()
                
    except Exception as e:
        print(f"Log init failed: {str(e)}")