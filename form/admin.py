from django.contrib import admin
from .models import *
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
     list_filter = ("category",)
     list_display = ("name", "type", "category")

admin.site.register(Category)
admin.site.register(Product, MyModelAdmin)
