import smtplib, ssl
from email.mime.text import MIMEText

class EmailSender():
    def __init__(self, port=465, smtp_server= "smtp.gmail.com", sender_email=None, password=None):
        self.port = port 
        self.smtp_server = smtp_server
        self.sender_email = sender_email
        self.password = password
    
    def send_email(self, receiver_email, random_code):
        body = f"인증코드 : {random_code}"
        message = MIMEText(body, "plain", "utf-8")
        message["Subject"] = "인증코드 보내드립니다."
        message["From"] = self.sender_email
        message["To"] = receiver_email

        context = ssl.create_default_context() 

        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, message.as_string())