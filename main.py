from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "support@answerdone.com"
password = "V{t5=jyB=Y{p"

SERVER = "64.31.43.242"
PORT = 465
EMAIL = "support@answerdone.com"
PASS = "V{t5=jyB=Y{p"


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/sendmail/")
async def login(ajax_name: Annotated[str, Form()], ajax_email: Annotated[str, Form()],ajax_message: Annotated[str, Form()]):
    message = MIMEMultipart("alternative")
    message["Subject"] = ajax_name+" => "+ajax_email
    message["From"] = sender_email
    message["To"] = ajax_email

    part1 = MIMEText(ajax_message, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("64.31.43.242", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, ajax_email, message.as_string()
        )
        return {"name": ajax_name,"email":ajax_email,"message":ajax_message}
