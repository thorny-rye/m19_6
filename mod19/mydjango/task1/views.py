from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator


# Create your views here.

def main_page(request):
    return render(request, "platform.html")


def catalog(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})


def purchases(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    Buyers = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                for buyer in Buyers:
                    if buyer.name == username:
                        info['error'] = "Пользователь уже существует"

                    else:
                        Buyer.objects.create(name=username, balance=1000, age=age)
                        return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    users = ["Petya", 'Kirill', 'Anton']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = "Пользователь уже существует"
        else:
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'registration_page.html', info)


def news(request):
    new = News1.objects.all()
    paginator = Paginator(new, 5)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_posts': page_posts})