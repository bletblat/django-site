from django import template
from main.models import MenuItem, Tabbs#, TabbItem
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context):
    menu_items = MenuItem.objects.filter(level=1)
    return {
        "menu_items": menu_items,
    }
@register.inclusion_tag('templatetags/tabb.html', takes_context=True)
# def show_tabb(context):
#     tabb_items = TabbItem.objects.filter(level=1)
#     return {
#         "menu_items": tabb_items,
#     }
def show_tabb(context):
    tabb_items = Tabbs.objects.all
    return {
        "tabb_items": tabb_items,
    }