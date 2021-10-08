from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Comment, Lesson, Course, Rate
import json

# Create your views here.


def home(request):
    if request.session.get('LOGGED_USER'):
        courses = Course.objects.all()
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
        course = Course.objects.get(id=id)
        lessons = Lesson.objects.filter(course=course)
        return render(request, 'course.html', {
            'course': course,
            'lessons': lessons,
            'logged_user': logged_user
        })
    else:
        return redirect('/auth/login?unauthorized_access=1')


def lesson(request, course_id, lesson_id):
    if request.session.get('LOGGED_USER'):
        logged_user = request.session.get('LOGGED_USER')
        lesson = Lesson.objects.get(id=lesson_id)
        comments = Comment.objects.filter(
            lesson_id=lesson_id).order_by('-created_at')

        request_user = request.session.get('LOGGED_USER')
        user_already_rates = Rate.objects.filter(
            lesson_id=lesson_id).filter(user_id=request_user)
        rates = Rate.objects.filter(lesson_id=lesson_id)

        return render(request, 'lesson.html', {
            'lesson': lesson,
            'logged_user': logged_user,
            'comments': comments,
            'request_user': request_user,
            'user_already_rates': user_already_rates,
            'rates': rates
        })
    else:
        return redirect('/auth/login?unauthorized_access=1')


def comment(request):
    user_id = int(request.POST.get('user_id'))
    description = request.POST.get('description')
    lesson_id = int(request.POST.get('lesson_id'))

    comment = Comment(user_id=user_id,
                      comment=description,
                      lesson_id=lesson_id)
    comment.save()

    comments = Comment.objects.filter(lesson=lesson_id).order_by('-created_at')
    only_names = [i.user.name for i in comments]
    only_comments = [i.comment for i in comments]
    comments = list(zip(only_names, only_comments))

    return HttpResponse(json.dumps({'status': '1', 'comments': comments}))


def rate(request):
    if request.session.get('LOGGED_USER'):

        rate = request.POST.get('rate')
        lesson_id = request.POST.get('lesson_id')

        user_id = request.session.get('LOGGED_USER')

        user_already_rates = Rate.objects.filter(
            lesson_id=lesson_id).filter(user_id=user_id)

        if not user_already_rates:
            rates = Rate(lesson_id=lesson_id,
                         rate=rate,
                         user_id=user_id,
                         )
            rates.save()
            return redirect(f'/home/course/{rates.lesson.course.id}/lesson/{rates.lesson.id}')

    else:
        return redirect('/auth/login?unauthorized_access=1')
