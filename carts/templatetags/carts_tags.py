from django import template

from carts.models import Carts

register = template.Library()

@register.simple_tag()
def user_carts(request):
    if request.user.is_authenticated:
        return Carts.objects.filter(user=request.user)
    