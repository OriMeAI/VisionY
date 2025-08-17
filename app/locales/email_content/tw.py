


def get_email_content(sign_number):
    return  {
        "subject": "驗證碼",
        "body": f"""
            <!DOCTYPE html>
            <html lang="tw">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>驗證碼</title>
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
                        <p>親愛的用戶</p>
                        <p>非常感謝您使用VisionY。請您使用下面的驗證碼完成登入：</p>
                        <div class="code">{sign_number}</div>
                        <p>該驗證碼10分鐘內有效。請您不要將驗證碼分享給他人。</p>
                        <p>如果不是您本人登入，請忽略本郵件或者聯繫開發團隊 contact@visiony.ai。</p>
                        <p>獻上深深的祝福</p>
                        <p>VisionY AI Team</p>
                    </div>
                    <div class="footer">
                        <p>© 2025 Orime. 版權所有。</p>
                    </div>
                </div>
            </body>
            </html>"""
    }