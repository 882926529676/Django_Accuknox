from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection

@receiver(pre_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    # Insert a row in the database in the signal handler
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO my_test_table (name) VALUES ('from_signal')")
    print("Signal handler executed.")

def save_user():
    try:
        with transaction.atomic():
            user = User(username="testuser")
            user.save()
            print("User save executed.")
            # Raising an exception to roll back the transaction
            raise Exception("Rolling back transaction")
    except Exception as e:
        print(e)

# Running the function
save_user()

# Checking if the data from the signal handler was rolled back
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM my_test_table WHERE name = 'from_signal'")
    result = cursor.fetchall()
    print("Rows in my_test_table:", result)
