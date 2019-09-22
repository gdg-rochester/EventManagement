import smtplib
import ssl
from email.mime.text import MIMEText


def send(data):
    print(data)
    port = 465  # For SSL
    password = "INSERT_PWD_HERE"

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.domain.com", port, context=context) as server:
        server.login("contact@gdgrochester.com", password)
        sender_email = "contact@gdgrochester.com"
        receiver_email = "contact@gdgrochester.com"
       

        bcc = ["neelkirit2@gmail.com", "narkhedesarang@gmail.com"]

        cont = '''{0}'''.format(data["message"])
        msgTo = ""
        text_receivers = ['contact@gdgrochester.com'
                          ]
        for person in text_receivers:
            msgTo += "{0} ".format(person)

        msg = MIMEText(cont, 'html')

        msg['Subject'] = '''{0}'''.format(data["subject"])
        msg['From'] = "GDG Rochester <contact@gdgrochester.com>"
        msg['To'] = msgTo
        receiver_email = [receiver_email] + bcc
        server.sendmail(sender_email, receiver_email, msg.as_string())
