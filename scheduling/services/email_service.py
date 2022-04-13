from django.core.mail import send_mail


def send_email(subject: None, message: None, from_: None, to_: None):
    return send_mail(
        subject=subject,
        message=message,
        from_email=from_,
        recipient_list=to_,
        fail_silently=False,
    )
