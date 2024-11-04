from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    info ={}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        print(username, password, repeat_password, age)

        if password == repeat_password and int(age) >=18 and username not in users:
            return HttpResponse(f'Приветсвуем, {username}!')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            info['error'] = 'Пользователь уже существует'

    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and int(age) >= 18 and username not in users:
                pass
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context=info)

