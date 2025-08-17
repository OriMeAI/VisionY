import httpx,os,logging
import asyncio
from app.locales.translations import get_translation
from app.utils.core import is_running_in_docker
import stripe

class Stripe:
    """
    https://dashboard.stripe.com/dashboard
    支付类，使用 Stripe Checkout
    
    测试卡号
    付款成功 4242 4242 4242 4242
    付款需要验证 4000 0025 0000 3155
    付款被拒绝 4000 0000 0000 9995
    
    """
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # 配置 PayPal SDK
        self.running_in_docker = is_running_in_docker()
        self.webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
        
        if self.running_in_docker:
            stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
            
            #这里对应 data/credits.py
            self.credit_item_id_to_price_id = {
                "credit_items_0":"price_1RpoECFd32ObwgBfk6cWEh8b", 
                "credit_items_1":"price_1Rq1QdFd32ObwgBf4X6ONUYg", 
                "credit_items_2":"price_1Rq1QkFd32ObwgBf49Injkoh", 
                "credit_items_3":"price_1Rq1QoFd32ObwgBfMXznJ2hz", 
                "credit_items_4":"price_1Rq1QrFd32ObwgBfJlJKP5rS", 
            }
            
            # 这里对应 data/membership.py
            self.membership_item_id_to_price_id = {
                "membership_items_1":"price_1Rq4QeFd32ObwgBfvI6O7ayo", 
                "membership_items_2":"price_1Rq4QgFd32ObwgBfpjTuSvsn", 
                "membership_items_4":"price_1Rq4QkFd32ObwgBf9YxdtNan", 
                "membership_items_5":"price_1Rq4QlFd32ObwgBfJA9Tz6yT",
            }
            
        else:
            stripe.api_key = os.getenv("STRIPE_SANDBOX_SECRET_KEY")
            
            # print(f"api_key is {stripe.api_key}")
            
            #这里对应 data/credits.py
            self.credit_item_id_to_price_id = {
                "credit_items_0":"price_1Rpo3oFvP3OJ7iSPfU91VYgl", 
                "credit_items_1":"price_1Rq1JYFvP3OJ7iSPCcw1LOe7", 
                "credit_items_2":"price_1Rq1K0FvP3OJ7iSPqZ3lP5ai", 
                "credit_items_3":"price_1Rq1KOFvP3OJ7iSPLR3oN7bi", 
                "credit_items_4":"price_1Rq1KkFvP3OJ7iSPiaBWZoUT", 
            }
            
            # 这里对应 data/membership.py
            self.membership_item_id_to_price_id = {
                "membership_items_1":"price_1Rq1Y2FvP3OJ7iSPxKPM4GP9", 
                "membership_items_2":"price_1Rq1YyFvP3OJ7iSPiPbLg1f4", 
                "membership_items_4":"price_1Rq1ZjFvP3OJ7iSPoUssN85o", 
                "membership_items_5":"price_1Rq1aOFvP3OJ7iSPkRDVLukc",
            }
                         
    def register_stripe(self):
        """
        注册 Stripe
        """            
        logging.info("Stripe Register Successfully")
        
    def create_payment(self, client_reference_id:str, item_code: str, success_url: str, cancel_url: str) -> dict:
        """
        创建积分购买支付
        result 为0 表明成功，result 为1 表明失败，msg说明失败情况
        """
        
        price_id = self.credit_item_id_to_price_id.get(item_code, "")
        
        if not price_id:
            logging.error(f"Payment creation failed： can not find price_id for item : {item_code}")
            return {"result": 1, "msg": get_translation("payment_creation_failed")}
        
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=client_reference_id,
                # currency="usd",
                line_items=[
                    {
                        # Provide the exact Price ID (for example, price_1234) of the product you want to sell
                        'price': price_id,
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
                automatic_tax={'enabled': True},
            )
                        
            return {"result": 0, "id":checkout_session.id, "url": checkout_session.url}

        except Exception as e:
            logging.error(f"Payment creation failed: {str(e)}", exc_info=True)
            return {"result": 1, "msg": get_translation("payment_creation_failed")}
        
    def capture_payment(self, stripe_id: str) -> dict:
        """
        捕获积分购买支付
        result 为0 表明成功，result 为1 表明失败，msg说明失败情况
        """        
        try:
            checkout_session = stripe.checkout.Session.retrieve(stripe_id)
            
            payment_status = checkout_session['payment_status']
                                        
            if payment_status == "paid":
                return {"result": 0, "checkout_session":checkout_session}
            else:
                return {"result": 1, "msg": get_translation("payment_capture_failed")}
                
        except Exception as e:
            logging.error(f"Payment capture failed: {str(e)}", exc_info=True)
            return {"result": 1, "msg": get_translation("payment_capture_failed")}

    def create_subscription(self, client_reference_id:str, item_code: str, success_url: str, cancel_url: str) -> dict:
        """
        创建订阅
        """
        
        price_id = self.membership_item_id_to_price_id.get(item_code, "")
        
        if not price_id:
            logging.error(f"Subscription creation failed： can not find price_id for item : {item_code}")
            return {"result": 1, "msg": get_translation("subscription_creation_failed")}
        
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=client_reference_id,
                line_items=[
                    {
                        # Provide the exact Price ID (for example, price_1234) of the product you want to sell
                        'price': price_id,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=success_url,
                cancel_url=cancel_url,
                automatic_tax={'enabled': True},
            )
                        
            return {"result": 0, "id":checkout_session.id, "url": checkout_session.url}
        except Exception as e:
            logging.error(f"Subscription creation failed: {str(e)}", exc_info=True)
            return {"result": 1, "msg": get_translation("subscription_creation_failed")}

    def verify_subscription(self, stripe_id: str) -> dict:
        """
        验证订阅状态
        """
        try:
            checkout_session = stripe.checkout.Session.retrieve(stripe_id)
            
            payment_status = checkout_session['payment_status']
                                        
            if payment_status == "paid":
                return {"result": 0, "checkout_session":checkout_session}
            else:
                return {"result": 1, "msg": get_translation("subscription_verification_failed")}
            
        except Exception as e:
            logging.error(f"Subscription verification failed: {str(e)}", exc_info=True)
            return {"result": 1, "msg": get_translation("subscription_verification_failed")}
        
    def verify_webhook_signature(self, payload, sig_header) -> bool:
        """
        验证 Stripe Webhook 签名
        """
        
        if not self.webhook_secret:
            logging.error(f"Stripe Webhook ID not found.  self.running_in_docker: {self.running_in_docker} Please check your configuration.")
            return False
        
        try:
            # 验证签名确保请求来自 Stripe
            event = stripe.Webhook.construct_event(
                payload, sig_header, self.webhook_secret
            )
            
            return {"result":0, "event":event}
                  
        except Exception as e:
            logging.error(f"Webhook verify signature failed: {str(e)}")
            return {"result":1}
        
# 创建单例实例
stripe_instance = Stripe()