
import threading
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")


def save_user():
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User(username="testuser")
    user.save()


save_user()
