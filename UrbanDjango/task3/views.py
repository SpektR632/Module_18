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
    return render(request, 'third_task/Home.html', context)


def shop(request):
    context = {
        'shop_text': "Игры",
        'game_name1': 'Atomic Heart',
        'game_name2': 'Cyberpunk 2027',
        'game_name3': 'PayDay 2',
        'buy': 'Купить',
        'back': 'Вернуться обратно'
    }
    return render(request, 'third_task/shop.html', context)


def cart(request):
    context = {
        'cart_text': "Корзина пуста, добавьте уже что-то!",
        'back': 'Вернуться обратно'
    }
    return render(request, 'third_task/basket.html', context)
