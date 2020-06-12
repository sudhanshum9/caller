from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.


class UserProfileManager(BaseUserManager):
    """to mamage user"""

    def create_user(self,phoneno,name,email,password=None):
        
        if not phoneno:
            raise ValueError('User must have phoneno')

        
        user= self.model(phoneno=phoneno,name=name,email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,phoneno,name,password,email):
        user = self.create_user(phoneno,name,password,email)

        user.is_superuser = True
        
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """to add user"""
    phoneno= models.IntegerField(unique=True)
    email = models.EmailField(max_length=40,blank=True)
    name= models.CharField(max_length=100)


    objects = UserProfileManager()

    USERNAME_FIELD ='phoneno'
    REQUIRED_FIELDS= ['name']


    
    def __str__(self):
        return self.name


class UserContacts(models.Model):
    """to add contacts"""
    user_profile= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE

    )
    phoneno= models.IntegerField(unique=True)
    email = models.EmailField(max_length=40,blank=True)
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.phoneno


class Spam(models.Model):
    """to add spam"""
    spam= models.IntegerField(unique=True)
      
    
    def __str__(self):
        return self.spam  



class GlobalData(models.Model):
    """to show all the data"""
    user_profile= models.ManyToManyField('UserProfile')

    usercontacts = models.ManyToManyField('UserContacts')
    spam = models.ManyToManyField('Spam')
