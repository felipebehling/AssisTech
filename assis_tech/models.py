from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

class MyAccountManager(BaseUserManager):
    def createuser(self, email, cpf, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            cpf=cpf
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    cpf = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, obg=None):
        return self.is_admin
    
