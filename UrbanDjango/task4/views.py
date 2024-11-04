from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def home(request):
    context = {
        'home_text': 'Главная страница',
        'home_page': 'Главная',
        'shop': 'Магазин',
        'cart': 'Корзина'
    }
    return render(request, 'fourth_task/Home.html', context)


def shop(request):
    context = {
        'shop_text': "Игры",
        'games': ['Atomic Heart', 'Cyberpunk 2027', 'PayDay 2'],
        'buy': 'Купить',
        'back': 'Вернуться обратно'
    }
    return render(request, 'fourth_task/shop.html', context)


def cart(request):
    context = {
        'cart': 'Корзина',
        'cart_text': "Корзина пуста, добавьте уже что-то!",
        'back': 'Вернуться обратно'
    }
    return render(request, 'fourth_task/basket.html', context)
