import smtplib
import ssl
import os
import asyncio # 确保导入 asyncio
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
from app.locales.translations import get_email_content

# 账户级别
smtp_server = os.environ.get("EMAIL_SMTP_SERVER", "")
smtp_port = os.environ.get("EMAIL_SMTP_PORT", "")
sender_mail = os.environ.get("EMAIL_SENDER_MAIL", "")
sender_name = os.environ.get("EMAIL_SENDER_NAME", "")
sender_password = os.environ.get("EMAIL_SENDER_PASSWORD", "")

# 修改函数定义为 async def
async def send_user_login_sign_number(email: str, sign_number: str) -> dict:
    """
    异步发送用户登录验证码邮件

    Args:
        email (str): 接收者邮箱地址
        sign_number (str): 验证码

    Returns:
        dict: 发送结果, 包含 'state' (0表示成功, 1表示失败) 和 'msg'
    """
    
    #测试服务器直接返回
    if smtp_server == "your_smtp_server":
        return {'state': 0, 'msg': 'Verification code sent to your email, please check'}
    
    email_content = get_email_content(sign_number)
    message = MIMEMultipart("alternative")
    # 使用 formataddr 来正确处理发件人姓名和地址，并进行 UTF-8 编码
    # 注意：SendEmail 类/对象需要在这个上下文有效，假设它是全局可访问的或已正确定义
    # 如果 SendEmail 是一个类，你需要实例化它或者确保属性是类属性
    # 这里假设 sender_name 和 sender_mail 是全局变量或来自某个配置对象
    message['From'] = formataddr((Header(sender_name, 'utf-8').encode(), sender_mail))
    message['To'] = email
    subject = f"{email_content['subject']}: {sign_number}"
    message['Subject'] = Header(subject, 'utf-8')

    # 格式化 HTML 内容
    html_body = email_content["body"]
    # 创建 HTML 部分
    part_html = MIMEText(html_body, 'html', 'utf-8')
    # 将 HTML 部分附加到 MIMEMultipart 对象
    message.attach(part_html)

    # aiosmtplib 默认使用 STARTTLS，对于端口 465 (SSL/TLS)，设置 use_tls=True
    try:
        # 使用 aiosmtplib 异步连接和发送
        async with aiosmtplib.SMTP(hostname=smtp_server, port=smtp_port, use_tls=True) as server:
            # await server.set_debuglevel(1) # 调试时取消注释
            # 假设 sender_mail 和 sender_password 是全局变量或来自配置
            await server.login(sender_mail, sender_password)
            # 使用 send_message 发送 email.message 对象
            await server.send_message(message)
        return {'state': 0, 'msg': 'Verification code sent to your email, please check'}
    except aiosmtplib.SMTPAuthenticationError as e:
        # aiosmtplib 复用了 smtplib 的异常类型
        return {'state': 1, 'msg': f"SMTP authentication failed: {e}"}
    except aiosmtplib.SMTPException as e:
        return {'state': 1, 'msg': f"Email sending failed: {e}"}
    except Exception as e:
        # 其他所有未知错误
        return {'state': 1, 'msg': f"An unknown error occurred: {e}"}

# # 示例用法 (需要在一个异步函数或事件循环中运行)
# async def main():
#     test_email = "recipient@example.com" # 替换为你的测试邮箱地址
#     test_code = "123456"
#     result = await send_user_login_sign_number(test_email, test_code)
#     print(result)

# if __name__ == '__main__':
#     asyncio.run(main())