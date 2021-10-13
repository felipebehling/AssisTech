from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from assis_tech.views import *


urlpatterns = [
  path('', views.index, name='index'),
  path('report/', views.report, name='report'),
  path('create/', views.create, name='create'),

  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
	path('dashboard/<user_id>/edit/', edit_account_view, name="edit-profile"),
  path('dashboard/<user_id>/edit/cropImage/', crop_image, name="crop_image"),
  
  path('dashboard/', views.dashboard, name='dashboard'),
  path('dashboard/detail/<int:pk>/', views.detail, name='detail'),
  path('dashboard/edit/<int:pk>/', views.edit, name='edit'),
  path('dashboard/update/<int:pk>/', views.update, name='update'),
  path('dashboard/delete/<int:pk>/', views.delete, name='delete'),
  path('dashboard/localization/<int:pk>/', views.localization, name='localization'),

  path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="pages/password_reset.html"),
     name="reset_password"),

  path('reset_password_sent/', 
      auth_views.PasswordResetDoneView.as_view(template_name="pages/password_reset_sent.html"), 
      name="password_reset_done"),

  path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="pages/password_reset_form.html"), 
    name="password_reset_confirm"),

  path('reset_password_complete/', 
      auth_views.PasswordResetCompleteView.as_view(template_name="pages/password_reset_done.html"), 
      name="password_reset_complete"),

]
