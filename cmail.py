'''import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,otp=False,subject=True,body=False):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('vaishnaviroyya123@gmail.com','cteyuzcshphzzypr')
    msg=EmailMessage()
    msg['From']='vaishnaviroyya123@gmail.com' 
    msg['Subject']=' Account signup for otp' if subject==False else subject
    msg['To']=to
    body=f'your one time otp for registration is {otp}' if body==False and otp!=False else body
    msg.set_content(body)
    server.send_message(msg)
    server.quit()'''




import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('vaishnaviroyya123@gmail.com ','cteyuzcshphzzypr')
    msg=EmailMessage()
    msg['From']='vaishnaviroyya123@gmail.com'
    msg['Subject']='Account signup for otp'
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()

    







        
    
