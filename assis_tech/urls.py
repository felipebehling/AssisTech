from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('report/', views.report, name='report'),
  path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
]

