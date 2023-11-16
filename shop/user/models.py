from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, email, user_name, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('User is not staff')

        return self.create_user(email, user_name, password, **other_fields)
    
    def create_user(self, email, user_name, password, **other_fields):
        
        if not email:
            raise ValueError(_('E-mail'))
            
        
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        

class UserBase(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('E-mail'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.user_name
    
    

    
    
    


