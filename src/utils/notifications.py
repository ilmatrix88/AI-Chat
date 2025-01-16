import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

def send_email_notification(subject, message):
    """
    Отправка уведомления по email.
    """
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")
    admin_email = os.getenv("ADMIN_EMAIL")

    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = admin_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Подключение к SMTP-серверу
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Включение TLS
            server.login(email_address, email_password)
            server.sendmail(email_address, admin_email, msg.as_string())
        print("Уведомление отправлено по email.")
    except Exception as e:
        print(f"Ошибка при отправке email: {e}")
