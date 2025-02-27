from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Дубок - Главная"
        context["content"] = "Магазин мебели Дубок"
        return context
    

class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Дубок - О нас"
        context["content"] = "О нас"
        context["text_on_page"] = "Магазин мебели Дубок"
        return context
    
        
# def index(request) -> HttpResponse:

#     categories = Categories.objects.all()

#     context: dict[str, str] = {
#         "title": "Дубок - Главная",
#         "content": "Магазин мебели Дубок",
#         "categories": categories,
#     }
#     return render(request, "main/index.html", context)


# def about(request) -> HttpResponse:
#     context: dict[str, str] = {
#         "title": "Дубок - О нас",
#         "content": "О нас",
#         "text_on_page": "Магазин мебели Дубок",
#     }
#     return render(request, "main/about.html", context)
