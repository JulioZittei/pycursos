from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('validate_registry/', views.validate_registry, name='validate_registry'),
    path('validate_login/', views.validate_login, name='validate_login')
]
