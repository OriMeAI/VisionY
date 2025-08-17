


def get_email_content(sign_number):
    return  {
        "subject": "認証コード",
        "body": f"""
            <!DOCTYPE html>
            <html lang="ja">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>認証コード</title>
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
                        <p>親愛なるユーザー様</p>
                        <p>VisionYをご利用いただき、誠にありがとうございます。以下の認証コードを使用してログインを完了してください：</p>
                        <div class="code">{sign_number}</div>
                        <p>この認証コードは10分間有効です。認証コードを他の人と共有しないでください。</p>
                        <p>このログイン試行がご本人によるものでない場合は、このメールを無視するか、開発チーム contact@visiony.ai までご連絡ください。</p>
                        <p>心よりお祈り申し上げます</p>
                        <p>The VisionY AI Team</p>
                    </div>
                    <div class="footer">
                        <p>© 2025 Orime. 全著作権所有。</p>
                    </div>
                </div>
            </body>
            </html>"""
    }