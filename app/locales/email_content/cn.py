


def get_email_content(sign_number):
    return  {
        "subject": "验证码",
        "body": f"""
            <!DOCTYPE html>
            <html lang="cn">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>验证码</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 0;
                    }}
                    .container {{
                        background-color: #ffffff;
                        margin: 50px auto;
                        padding: 20px;
                        border: 1px solid #dddddd;
                        border-radius: 5px;
                        max-width: 600px;
                    }}
                    .header {{
                        text-align: center;
                        padding: 20px;
                        background-color: #7E2FFF;
                        color: #ffffff;
                        border-top-left-radius: 5px;
                        border-top-right-radius: 5px;
                    }}
                    .content {{
                        padding: 20px;
                        text-align: center;
                    }}
                    .content p {{
                        font-size: 16px;
                        line-height: 1.6;
                    }}
                    .code {{
                        display: inline-block;
                        background-color: #f7f7f7;
                        padding: 10px 20px;
                        font-size: 24px;
                        color: #333333;
                        border: 1px solid #dddddd;
                        margin: 20px 0;
                    }}
                    .footer {{
                        text-align: center;
                        padding: 20px;
                        font-size: 12px;
                        color: #aaaaaa;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>VisionY AI</h1>
                    </div>
                    <div class="content">
                        <p>亲爱的用户</p>
                        <p>非常感谢您使用VisionY。 请您使用下面的验证码完成登录:</p>
                        <div class="code">{sign_number}</div>
                        <p>该验证码10分钟内有效。 请您不要将验证码分享给他人。</p>
                        <p>如果不是您本人登录, 请忽略本邮件或者联系开发团队 contact@visiony.ai。</p>
                        <p>献上深深的祝福</p>
                        <p>VisionY AI Team</p>
                    </div>
                    <div class="footer">
                        <p>© 2025 Orime. 版权所有。</p>
                    </div>
                </div>
            </body>
            </html>"""
    }