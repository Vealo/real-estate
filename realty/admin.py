from django.contrib import admin
from . import models

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'description', 'space']
    list_filter = ['id', 'type', 'description', 'space']
    search_fields = ['type', 'description']
    ordering = ['type', 'description']


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(models.BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Сountrie)
class СountrieAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'abbreviations']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.RegionCode)
class RegionCodeAdmin(admin.ModelAdmin):
    list_display = ['code']
    list_filter = ['code']
    search_fields = ['code']

@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviations']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}