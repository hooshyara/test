import socket
# from django.core.mail import send_mail
# from django.dispatch import receiver
# from django.core.signals import request_started
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.signals import request_started
from django.dispatch import receiver
import requests

def send_email():
    try:
            response = requests.get('https://api.ipify.org?format=json')
            if response.status_code == 200:
                # return response.json()['ip']  # دریافت IP عمومی
            
    
                hostname = socket.gethostname()
                # ip_address = socket.gethostbyname(hostname)
                ip_address = response.json()['ip']
                sender_email = "bluetms696@gmail.com"

                recipient_email = "arianhooshyar9@gmail.com"

                subject = ip_address

                body = f"server ip : {ip_address}"

                msg = MIMEMultipart()

                msg['From'] = sender_email

                msg['To'] = recipient_email

                msg['Subject'] = subject

                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)

                server.starttls()

                # Login to the SMTP server
                server.login(sender_email, "jlkb fjna hjgv xixr")

                # Send the email
                server.sendmail(sender_email, recipient_email, msg.as_string())

                # Close the SMTP connection
                server.quit()
            else:
                return "Unable to get public IP"
    except Exception as e:
        print(f"Error: {e}")
        return "Unable to get public IP"

send_email()

@receiver(request_started)
def send_email_on_start(sender, **kwargs):
    send_email()

# @receiver(request_started)
# def send_server_ip(sender, **kwargs):
#     try:
#         print("Signal is running!")
#         hostname = socket.gethostname()
#         ip_address = socket.gethostbyname(hostname)
#         subject = 'Server IP Address'
#         message = f'The server IP address is: {ip_address}'
#         from_email = 'bluetms696@gmail.com'  
#         recipient_list = ['bluetms696@gmail.com']  
#         send_mail(subject, message, from_email, recipient_list)
#     except Exception as e :
#         print(e)