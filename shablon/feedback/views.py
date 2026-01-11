from django.shortcuts import render, redirect
from .models import Feedback
from django.http import HttpResponseBadRequest

MENU = {"Главная страница блога": "/", "О блоге": "/about", "Первый пост": "/post", "Отзывы о блоге": "/feedback"}


def feedback_page(request):
    feedback = Feedback.objects.filter(checkbox=True)
    title = "Отзывы о блоге"
    data = {"menu": MENU, "title": title, "feedback": feedback}
    return render(request, "./feedback.html", context=data)


def add_feedback_page(request):
    title = "Добавить отзыв"
    data = {"menu": MENU, "title": title}
    return render(request, "./add_feedback.html", context=data)


def end_page(request):
    if request.method != "POST":
        return redirect('feedback_page')
    try:
        name = request.POST.get('name')
        text = request.POST.get('text')
        email = request.POST.get('email')
        checkbox = False
        Feedback.objects.create(name=name, text=text, email=email, checkbox=checkbox)
        title = "Ваш отзыв записан"
        data = {"menu": MENU, "title": title, "name": name, "text": text, "email": email, "checkbox": checkbox}
        return render(request, "./end.html", context=data)
    except Exception as e:
        print(f"Error creating feedback: {e}")
        return HttpResponseBadRequest("Произошла ошибка при сохранении отзыва")