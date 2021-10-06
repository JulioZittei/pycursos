from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/<int:id>', views.course, name='course'),
    path('course/<int:course_id>/lesson/<int:lesson_id>',
         views.lesson, name='lesson'),
]
