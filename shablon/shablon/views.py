from django.http import HttpResponse
from django.shortcuts import render


MENU = {"Главная страница блога": "/", "О блоге": "/about", "Первый пост": "/post", "Отзывы о блоге": "/feedback"}

def main_page(request):
    title = "Главная страница блога"
    data = {"menu":MENU, "title":title}
    return render(request, "./index.html", context=data)

def about_page(request):
    title = "О блоге"
    data = {"menu":MENU, "title":title}
    return render(request, "./about.html", context=data)
