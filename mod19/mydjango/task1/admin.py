from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost',)
    list_display = ('title', 'cost', 'size',)
    search_fields = ('title',)
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)
    list_display = ('name', 'balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)

@admin.register(News1)
class NewsAdmin1(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    list_filter = ('title', 'content')
    search_fields = ('title', 'content')
