from django.shortcuts import render
from .models import Summer

MENU = {"Главная страница блога": "/", "О блоге": "/about", "Первый пост": "/post", "Отзывы о блоге": "/feedback"}

def post_page(request):
    summer = Summer.objects.all()
    title = "Как я провела лето 2025"
    data = {"menu":MENU, "title":title, "summer":summer}
    return render(request, "./post.html", context=data)
