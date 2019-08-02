import smtplib
import ssl
from email.mime.text import MIMEText


def send(data):
    print(data)
    port = 465  # For SSL
    password = "Bakchod!@#$56"

    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.domain.com", port, context=context) as server:
        server.login("contact@gdgrochester.com", password)
        sender_email = "contact@gdgrochester.com"
        receiver_email = "neelkirit2@gmail.com"
        message = """\
            Subject: Hi there

            This message is sent from Python."""

        cont = '''\
                   <html>
                     <head></head>
                     <body>
                       <p>{0}</p>
                     </body>
                   </html>
                   '''.format(data['message'])

        msgTo = ""
        text_receivers = ['neelkirit2@gmail.com'
                          ]
        for person in text_receivers:
            msgTo += "{0} ".format(person)

        msg = MIMEText(cont, 'html')

        msg['Subject'] = "Hello"
        msg['From'] = "GDG Rochester <contact@gdgrochester.com>"
        msg['To'] = msgTo
        server.sendmail(sender_email, receiver_email, msg.as_string())
