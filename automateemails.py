#My Youtube Channel:     iitian sid
#if you want to understand about the code you can visit my youtube channel and search for Automate Gmail Using Python.........
import os
from email.message import EmailMessage
import ssl#for secure transmission of messages
import smtplib#sipmle mail transfer protocol library for sending mail by functions
email_sender='testmail@gmail.com'
email_password='XXXXXXXXXX'
email_reciever='testmamil2@gmail.com'
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
