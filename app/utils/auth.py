from authlib.integrations.starlette_client import OAuth
import os,logging

class Auth:
    """
    认证类 
    """
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        初始化
        """
        self.oauth = OAuth()
        # self.register_google_auth()  # ✅ 初始化时就注册
        
    def register_google_auth(self):
        """
        # 注册 Google 登录
        """
        self.oauth.register(
            name="google",
            client_id=os.getenv("GOOGLE_CLIENT_ID"),
            client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
            server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
            client_kwargs={"scope": "openid email profile"},
        )
        
        logging.info("Google Auth Register Successfully")
        
auth_instance = Auth()
