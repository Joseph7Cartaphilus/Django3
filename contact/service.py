from django.core.mail import send_mail


def send(user_email):
    send_mail(
        "Вы подписались на рассылку",
        "Тут текст",
        "cellerycandy17@gmail.com",
        [user_email],
        fail_silently=False,
    )
