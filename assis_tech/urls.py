from django.urls import path
from . import views

from assis_tech.views import *


urlpatterns = [
  path('', views.index, name='index'),
  path('report/', views.report, name='report'),
  path('create/', views.create, name='create'),

  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
  path('dashboard/<user_id>/', account_view, name="view"),
	path('dashboard/<user_id>/edit/', edit_account_view, name="edit-profile"),
  path('dashboard/<user_id>/edit/cropImage/', crop_image, name="crop_image"),
  
  path('dashboard/', views.dashboard, name='dashboard'),
  path('dashboard/detalhe/<int:pk>/', views.detail, name='detail'),
  path('dashboard/editar/<int:pk>/', views.edit, name='edit'),
  path('dashboard/atualizar/<int:pk>/', views.update, name='update'),
  path('dashboard/deletar/<int:pk>/', views.delete, name='delete'),

  path('dados/', views.dados, name='dados'),
]
