import os
from email.message import EmailMessage
import ssl
import smtplib
email_sender='siddhantsaxena2881@gmail.com'
email_password='plbuuqcbxutufuxn'
email_reciever=['saxenasid2132002@gmail.com','siddhantsaxena0786@gmail.com']
subject='Test Mail'
body="""
Hello,This is Siddhant Saxena And This Mail Is Only For Testing Purpose.Just Ignore It.
"""
em=EmailMessage()
em['from']=email_sender
em['to']=email_reciever
em['Subject']=subject
em.set_content(body)
context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:#smpts on port 465
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())