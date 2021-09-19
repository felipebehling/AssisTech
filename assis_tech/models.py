from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Usuarios precisam ter um email!')
		if not username:
			raise ValueError('Usuarios precisam ter um nome!')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


def get_profile_image_filepath(self, filename): #Altera o nome da imagem recebida pelo usuario e transforma em um padrão(só muda a pk sendo única para cada um).
	return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():	#Caso a pessoa não coloque uma foto
	return "img/AssisTech.png"


class Account(AbstractBaseUser): #Campos como is_admin, is_active, is_staff, is_superuser são obrigatorios para criar um model de usuario
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	cpf 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	profile_image			= models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True, default=get_default_profile_image)
	hide_email				= models.BooleanField(default=True)

	USERNAME_FIELD = 'email' #Altera a Forma de login principal(vem por padrão username).
	REQUIRED_FIELDS = ['username', 'cpf'] #Coloque dentro do colchetes os campos obrigatórios.

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	def get_profile_image_filename(self):
		return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

	# Para verificar as permissões, todos os administradores têm TODAS as permissões. BRABO DMS
	def has_perm(self, perm, obj=None):
		return self.is_admin

	#Este usuário tem permissão para visualizar este aplicativo? (SEMPRE SIM PARA SIMPLICIDADE)
	def has_module_perms(self, app_label):
		return True