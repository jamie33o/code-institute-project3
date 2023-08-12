from email.message import EmailMessage
import ssl
import smtplib
import os
import json

email_cred = os.environ.get("EMAIL_CREDS")
email_cred_dict = json.loads(email_cred)


def send_email():

    email_sender = email_cred_dict.get("email_sender")
    email_password = email_cred_dict.get("email_password")

    email_receiver = "giftsforyou83@gmail.com"

    subject = "Bingo books"
    body = "Books ddkd"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
