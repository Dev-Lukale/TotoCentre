
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# accounts.models.py

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, user_name,email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not user_name:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, user_name,email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            user_name,
            email,
            
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            user_name,
            email, 
            
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    user_name=models.CharField(max_length=200,blank=True,null=True,) 
    email = models.EmailField(max_length=255,unique=True,)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False)

    objects = UserManager()
     # a superuser
    # notice the absence of a "Password field", that's built in.
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name'] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.user_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.user_name} Profile'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
