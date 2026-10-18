import smtplib
from email.message import EmailMessage

def send(to, subject, body, smtp_user, smtp_pass):
    msg = EmailMessage()
    msg["Subject"], msg["From"], msg["To"] = subject, smtp_user, to
    msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
        s.login(smtp_user, smtp_pass)
        s.send_message(msg)
    print("Sent!")

if __name__ == "__main__":
    send(
        input("To: "), input("Subject: "), input("Body: "),
        input("Your email: "), input("App password: ")
    )
