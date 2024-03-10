from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, **kwargs):

        if not username:
            raise ValueError("Users must have an email address")

        user = self.model(
            username=username,
            phone_number=phone_number,
            **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):

        user = self.create_user(
            username,
            '',
            password=password,

        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length= 13, null= False, blank= False)
    username = models.CharField(max_length= 20, null= False, blank= False, unique= True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
