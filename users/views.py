from django.shortcuts import render

from users.forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context: dict[str, str] = {
        'title': 'Дубок - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context=context)


def registration(request):
    context: dict[str, str] = {
        'title': 'Дубок - Регистрация',
    }
    return render(request, 'users/registration.html', context=context)


def profile(request):
    context: dict[str, str] = {
        'title': 'Дубок - Кабинет',
    }
    return render(request, 'users/profile.html', context=context)


def logout(request):
    context: dict[str, str] = {
        'title': 'Дубок - Выход',
    }
    return render(request, 'users/logout.html', context=context)