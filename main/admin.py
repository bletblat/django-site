from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from main.models import MenuItem, Tabbs#, TabbItem


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(MenuItem, MenuItemMPTTModelAdmin)
admin.site.register(Tabbs)


# class TabbItemMPTTModelAdmin(MPTTModelAdmin):
#     mptt_level_indent = 40

# admin.site.register(TabbItem, TabbItemMPTTModelAdmin)