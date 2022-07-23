from django.contrib import admin
from .models import Categories


@admin.register(Categories)
class CommodityAdmin(admin.ModelAdmin):
    model = Categories