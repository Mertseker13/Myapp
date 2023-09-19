from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username1 = request.POST['username1']
        password = request.POST['password']

        user = auth.authenticate(username1=username1, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Неверные Данные')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username1 = request.POST['username1']
        email1 = request.POST['email1']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username1).exists():
                messages.info(request, 'Имя Пользователя Занято')
                return redirect('register')
            elif User.objects.filter(email=email1).exists():
                messages.info(request, 'Почта Занята')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username1, password=password, email=email1)
                user.save()
                print('USER CREATED')
                return redirect('/')
        else:
            messages.info(request, 'Пароль Не Совпадает!!!!!')
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
