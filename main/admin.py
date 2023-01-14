from django.contrib import admin
from .models import Home, Relevance, Skills, Geography, LastVacancies


@admin.register(Home)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Relevance)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Geography)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Skills)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(LastVacancies)
class HomePage(admin.ModelAdmin):
    list_display = ('title',)
