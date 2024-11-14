


import time
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulate a delay to demonstrate synchronous behavior
    print("Signal handler finished.")

# Simulate saving a user instance
def save_user():
    print("Save started.")
    user = User(username="testuser")
    user.save()
    print("Save finished.")

# Running the function
save_user()
