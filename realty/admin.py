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
    search_fields = ['name', 'discription']
    ordering = ['name']


@admin.register(models.BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Countrie)
class CountrieAdmin(admin.ModelAdmin):
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

@admin.register(models.Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(models.StreetType)
class StreetTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviations']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(models.SectionType)
class SectionTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(models.EntranceType)
class EntranceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(models.Entrance)
class EntranceAdmin(admin.ModelAdmin):
    list_display = ['numbers']
    list_filter = ['numbers']
    search_fields = ['numbers']

@admin.register(models.EntranceSpecial)
class EntranceSpecialAdmin(admin.ModelAdmin):
       list_display = ['name']
       list_filter = ['name']
       search_fields = ['name', 'description']

@admin.register(models.Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'description']

@admin.register(models.Ladder)
class Ladder(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'description']

@admin.register(models.FloorSpecial)
class FloorSpecialAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'description']

@admin.register(models.SpaceType)
class SpaceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name', 'discription']

@admin.register(models.Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['index', 'country', 'region', 'locality', 'street_type', 'street', 'building_number']
    list_filter = ['index', 'country', 'region', 'locality', 'street_type', 'street', 'building_number']
    search_fields =['index', 'country', 'region', 'locality', 'street_type', 'street', 'building_number']

@admin.register(models.Section)
class Section(admin.ModelAdmin):
    list_display = ['number', 'section_type', 'entrance_special', 'description', 'building', 'max_number_of_floors']
    list_filter = ['number', 'section_type', 'entrance_special', 'description', 'building', 'max_number_of_floors']
    search_fields = ['number', 'section_type', 'entrance_special', 'description', 'building', 'max_number_of_floors']

@admin.register(models.Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ['number', 'ladder', 'elevator', 'section']
    list_filter = ['number', 'ladder', 'elevator', 'section']
    search_fields = ['number', 'ladder', 'elevator', 'section']

@admin.register(models.Space)
class SpaceAdmin(admin.ModelAdmin):
    list_filter = ['space_type', 'number', 'square', 'description']
    list_display = ['space_type', 'number', 'square', 'description']
    search_fields = ['space_type', 'number', 'square', 'description']