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
        receiver_email = "contact@gdgrochester.com"
        # bcc = [
        #     "lmontedoro@gmail.com",
        #     "jnafus@frontiernet.net",
        #     "davidryanbarnard@gmail.com",
        #     "adarshreddy.r@gmail.com",
        #     "abhilash@theagileschool.com",
        #     "priyankarajan2590@gmail.com",
        #     "fbfmcote@gmail.com",
        #     "vrodriguez@itx.com",
        #     "asmita231@gmail.com",
        #     "ishiika.prasad@gmail.com",
        #     "dfwarden@gmail.com",
        #     "todd@toddbernhard.com",
        #     "vganesh@paychex.com",
        #     "kedargn94@gmail.com",
        #     "ksjacques@paychex.com",
        #     "virajchaudhari.2016@gmail.com",
        #     "abrown@paychex.com",
        #     "maxherman@gmail.com",
        #     "drb4637@gmail.com",
        #     "c.abhilash@gmail.com",
        #     "jlad521@gmail.com",
        #     "justin.z.tang94@gmail.com",
        #     "phansen@paychex.com",
        #     "Mhodesty@gmail.com",
        #     "wangchoumi@gmail.com",
        #     "pjwilbur99@gmail.com",
        #     "zmyaro@zmyaro.com",
        #     "Adityalandge1994@gmail.com",
        #     "Darwyncook@gmail.com",
        #     "mjohnson2898@gmail.com",
        #     "omkarvaidya13@gmail.com",
        #     "georgecolgrove@gmail.com",
        #     "priyapriya2590@gmail.com",
        #     "ayushsoni638@gmail.com",
        #     "ikunal03@gmail.com",
        #     "ayushipatra369@gmail.com",
        #     "ashwini.jaitapkar9@gmail.com",
        #     "junaidazharshaikh@gmail.com",
        #     "ssuloglu@gmail.com",
        #     "ajinkyarode3@gmail.com",
        #     "pwagh@buffalo.edu",
        #     "sanyuktakate@gmail.com",
        #     "chandak.kishor14@gmail.com"
        #     ]

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
