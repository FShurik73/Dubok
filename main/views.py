from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request) -> HttpResponse:

    categories = Categories.objects.all()

    context: dict[str, str] = {
        "title": "Дубок - Главная",
        "content": "Магазин мебели Дубок",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    context: dict[str, str] = {
        "title": "Дубок - О нас",
        "content": "О нас",
        "text_on_page": "Магазин мебели Дубок",
    }
    return render(request, "main/about.html", context)
