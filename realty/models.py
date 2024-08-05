from django.db import models
from django.utils import timezone
import uuid

#Справочники
#Тип дома
class TepyBuildings(models.Model):
    type = models.CharField(max_length=50,help_text="Наименование")
    description = models.CharField(max_length=250, help_text="Описание")
# Страны
class Сountries(models.Model):
    full_name = models.CharField(max_length=100, help_text="Название страны")
    abbreviations = models.CharField(max_length=4, help_text="Абривиатура")

#Код субъекта
class CodeRegions(models.Model):
    code = models.CharField(max_length=4, help_text="Код региона")
#Субъект
class Regions(models.Model):
    full_name = models.CharField(max_length=100, help_text="Название субьекта")
    abbreviations = models.CharField(max_length=4, help_text="Абривиатура")
    code = models.ForeignKey(CodeRegions, help_text="Код региона")

#Модели
class Buildings(models.Model):
    '''
    Здание
    - Адрес
    - Тип строения
    - Этажность
    - Площадь
    - Описание
    '''
    #Adress
    index = models.CharField(max_length=10, help_text="Индекс")
    country = models.OneToOneField(Сountries, on_delete=models.SET_NULL, help_text="Страна")
    region = models.OneToOneField(Regions, on_delete=models.SET_NULL, help_text="Субъект")

    #Common
    type = models.OneToOneField(TepyBuildings, on_delete=models.SET_NULL, help_text="Тип дома")
    total_space = models.IntegerField(help_text="Этажность")
    total_square = models.FloatField(help_text="Общая площадь")
    description = models.CharField(help_text="Описание")
