import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('vaishnaviroyya123@gmail.com',
    msg=EmailMessage()
    msg['From']='vaishnaviroyya123@gmail.com', 'cteyuzcshphzzypr')
    msg['Subject']=' Account signup for otp'
    msg['To']=to
    body=f'your one time otp for registration is (otp)'
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
