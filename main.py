import smtplib
from email.message import EmailMessage

sender_email = "mariyanichiporuk643@yandex.ru"
recipient_mail = "mariyanichiporuk643@gmail.com"
password = "rcnbvcqquwjxkkhx"
subject = "Проверка связи!"
body = "Привет из программы на питоне"

msg = EmailMessage()
msg.set_content(body)
msg["Subject"] = subject
msg["From"] =sender_email
msg["To"] = recipient_mail

try:
    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print("Письмо отправлено!")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    if server:
        server.quit()