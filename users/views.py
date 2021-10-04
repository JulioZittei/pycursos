from django.http.response import HttpResponse
from django.shortcuts import render
from .models import User
from django.shortcuts import redirect
import hashlib

# Create your views here.


def register(request):
    required_fields = request.GET.get('required_fields')
    user_exists = request.GET.get('user_exists')
    invalid_password = request.GET.get('invalid_password')
    success = request.GET.get('success')
    return render(request, 'register.html', {
        'required_fields': required_fields,
        'user_exists': user_exists,
        'invalid_password': invalid_password,
        'success': success
    })


def login(request):
    return render(request, 'login.html')


def validate_registry(request):
    errors = []
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user_exists = User.objects.filter(email=email)

    if len(name.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
        errors.append('required_fields=1')

    if len(user_exists) > 0:
        errors.append('user_exists=1')

    if len(password) < 8 or len(password) > 12:
        errors.append('invalid_password=1')

    if len(errors) > 0:
        splited_errors = "&".join(errors)
        errors.pop
        return redirect(f'/auth/register?{splited_errors}')

    try:
        password = hashlib.sha256(password.encode()).hexdigest()
        user = User(name=name, email=email, password=password)
        user.save()
    except:
        return HttpResponse('500 - Internal Server Error')

    return redirect('/auth/register?success=1')
