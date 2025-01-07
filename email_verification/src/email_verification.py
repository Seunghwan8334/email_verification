from random_code_generator import generate_code
from send_email import EmailSender

from dotenv import load_dotenv
import os 

from send_email import EmailSender

load_dotenv()
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
password = os.getenv("APP_PASSWORD")


class EmailVerification():
    def __init__(self):
        self.verification_code = None 
        self.verified = False 

    def verify(self, receiver_email):
        email_sender = EmailSender(sender_email=sender_email, password=password)
        self.verification_code = generate_code()
        email_sender.send_email(receiver_email=receiver_email, random_code=self.verification_code)
        self.input_code()

    def input_code(self):

        for _ in range(3):
            print("인증 코드를 입력하세요: ")
            code = input()
            if code == self.verification_code:
                print("확인되었습니다.")
                self.verified = True
                break
            else:
                print("틀렸습니다.")
            
        if self.verified == True:
            print("사이트로 이동합니다.")
        else:
            print("3회 이상 틀렸습니다.")

emailverification = EmailVerification()
emailverification.verify(receiver_email)
        
        

