from movies_project.celery import app
from django.core.mail import send_mail

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            "Вы подписались на рассылку",
            "Мы будем присылать спам каждый 10 минут",
            "cellerycandy17@gmail.com",
            [contact.email],
            fail_silently=False,
        )


@app.task
def send_notification(user_email):
    print(f"Уведомление отправлено контакту {user_email}")
