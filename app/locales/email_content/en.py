


def get_email_content(sign_number):
    return  {
        "subject": "Verification Code",
        "body": f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Verification Code</title>
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
                        <p>Dear User,</p>
                        <p>Thank you for using VisionY. Please use the verification code below to complete your login:</p>
                        <div class="code">{sign_number}</div>
                        <p>This verification code is valid for 10 minutes. Please do not share the verification code with others.</p>
                        <p>If this login attempt was not made by you, please ignore this email or contact our development team at contact@visiony.ai.</p>
                        <p>Best regards,</p>
                        <p>VisionY AI Team</p>
                    </div>
                    <div class="footer">
                        <p>© 2025 Orime. All Rights Reserved.</p>
                    </div>
                </div>
            </body>
            </html>"""
    }