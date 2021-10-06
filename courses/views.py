from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Classes, Courses

# Create your views here.


def home(request):
    if request.session.get('LOGGED_USER'):
        courses = Courses.objects.all()
        logged_user = request.session.get('LOGGED_USER')
        return render(request, 'home.html', {
            'courses': courses,
            'logged_user': logged_user
        })
    else:
        return redirect('/auth/login?unauthorized_access=1')


def course(request, id):
    if request.session.get('LOGGED_USER'):
        logged_user = request.session.get('LOGGED_USER')
        course = Courses.objects.get(id=id)
        classes = Classes.objects.filter(course=course)
        return render(request, 'course.html', {
            'course': course,
            'classes': classes,
            'logged_user': logged_user
        })
    else:
        return redirect('/auth/login?unauthorized_access=1')


def lesson(request, course_id, lesson_id):
    if request.session.get('LOGGED_USER'):
        logged_user = request.session.get('LOGGED_USER')
        course = Courses.objects.get(id=course_id)
        lesson = Classes.objects.get(id=lesson_id)
        return render(request, 'lesson.html', {
            'course': course,
            'lesson': lesson,
            'logged_user': logged_user
        })
    else:
        return redirect('/auth/login?unauthorized_access=1')
