from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    class Meta:
        swappable = 'AUTH_USER_MODEL'
