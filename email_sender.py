from email.message import EmailMessage
import ssl
import smtplib
import os

# my email and password
PW = os.environ.get("PW")
SENDER_EMAIL= os.environ.get("SENDER_EMAIL")

def send_email(email, file_name,pdf_buffer):
    """Sends email to user"""
    email_sender = SENDER_EMAIL
    email_password = PW
    
    email_receiver = email

    subject = "Bingo books"
    body = "Books ddkd"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)
    # add the PDF buffer as an attachment
    pdf_attachment = pdf_buffer.getvalue()
    em.add_attachment(pdf_attachment, filename=file_name, maintype="application", subtype="pdf")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
