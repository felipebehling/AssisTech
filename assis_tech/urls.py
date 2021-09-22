from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('report/', views.report, name='report'),
  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('dashboard/detalhe/<int:pk>/', views.detail, name='detail'),
  path('dashboard/editar/<int:pk>/', views.edit, name='edit'),
  path('dashboard/atualizar/<int:pk>/', views.update, name='update'),
  path('dashboard/deletar/<int:pk>/', views.delete, name='delete'),
]

