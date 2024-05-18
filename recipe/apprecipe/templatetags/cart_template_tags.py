from django import template
from apprecipe.models import Recipe

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Recipe.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0