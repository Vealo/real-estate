from django.db import models
import uuid

#Справочники
class BuildingType(models.Model):
    """Справочник типов строений"""
    type = models.CharField(max_length=50,help_text="Наименование")
    description = models.CharField(max_length=250, help_text="Описание")


class Сountrie(models.Model):
    """Справочник стран"""
    name = models.CharField(max_length=100, help_text="Название страны")
    abbreviations = models.CharField(max_length=4, help_text="Абривиатура")



class RegionCode(models.Model):
    "Справочник код субъектов"
    code = models.CharField(max_length=4, help_text="Код региона")


class Region(models.Model):
    """Справочник субъектов"""
    name = models.CharField(max_length=100, help_text="Название субъекта")
    abbreviations = models.CharField(max_length=4, help_text="Абривиатура")
    code = models.ForeignKey(RegionCode, help_text="Код региона")


class Locality(models.Model):
    """Справочник начеленных пунктов    """
    name = models.CharField(max_length=250, help_text="Назвение населенного пункта")


class StreetType(models.Model):
    """Справочник типов дорог в населенном пункте. Пример: улица."""
    name = models.CharField(max_length=100, help_text="Тип дороги (улицы) в городе")
    abbreviations = models.CharField(max_length=6, help_text="Абривиатура названия")


class BuildingType(models.Model):
    """Тип строения."""
    name = models.CharField(max_length=150, help_text="Наименование типа строения")
    description = models.TextField(help_text="Описание строения")


class SectionType(models.Model):
    """Справочник типов секций"""
    name = models.CharField(max_length=50, help_text="Наименование секции")


class EntranceType(models.Model):
    """Справочник типов входов"""
    name = models.CharField(max_length=50, help_text="Тип входа (парадная / подъезд)")


class Entrance(models.Model):
    """Справочник входов"""
    entrance_type = models.OneToOneField(EntranceType, help_text="Тип входа")
    numbers = models.CharField(max_length=10, help_text="Номер входа")
    description = models.TextField(help_text="Описание")


class EntranceSpecial(models.Model):
    """Нестандартных справочников входов"""
    name = models.CharField(max_length=150, help_text="Наименование входа")
    description = models.TextField(help_text="Описание")


class Elevator(models.Model):
    """Справочник лифтов"""
    name = models.CharField(max_length=150, help_text="Название лифта")
    description = models.TextField(help_text="Описание")


class Ladder(models.Model):
    """Справочник лесница"""
    name = models.CharField(max_length=150, help_text="Название лесница")
    description = models.TextField(help_text="Описание")

#Миксины
class BaseTime(models.Model):
    "Класс миксин - создание, изменение"
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


#Модели
class Building(models.Model, BaseTime):
    """
    Здание
    - Адрес
    - Тип строения
    - Этажность
    - Площадь
    - Описание
    """
    #Adress
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    index = models.CharField(max_length=10, help_text="Индекс")
    country = models.OneToOneField(Сountrie, on_delete=models.SET_NULL, help_text="Страна")
    region = models.OneToOneField(Region, on_delete=models.SET_NULL, help_text="Субъект")
    locality = models.OneToOneField(Locality, on_delete=models.SET_NULL, help_text="Начеленный пункт")
    street_type = models.OneToOneField(StreetType, on_delete=models.SET_NULL, help_text="Тип дороги")
    street = models.CharField(max_length=250, help_text="Название дороги (улицы)")
    building_type = models.OneToOneField(BuildingType, on_delete=models.SET_NULL, help_text="Тип строения")
    building_number = models.CharField(max_length=10, help_text="Номер сроения")

    #Common
    type = models.OneToOneField(BuildingType, on_delete=models.SET_NULL, help_text="Тип дома")
    total_space = models.IntegerField(help_text="Этажность")
    total_square = models.FloatField(help_text="Общая площадь")
    description = models.CharField(help_text="Описание")


    class Meta:
        ordering = ["-created"]

class Section(models.Model, BaseTime):
    """Секция дома."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(help_text="Номер секции")
    section_type = models.OneToOneField(SectionType, on_delete=models.SET_NULL, help_text="Тип секции")
    entrance_special = models.ForeignKey(EntranceSpecial, help="")
    description = models.TextField(help_text="Описание секции")
    building = models.ForeignKey(Building, help_text="Дом")
    max_number_of_floors = models.IntegerField(help_text="Этажность")

    class Meta:
        ordering = ['number']

class Floor(models.Model, BaseTime):
    """Этаж секции"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(help_text="Номер этажа")
    ladder = models.ForeignKey(Ladder, help_text="Лифт", on_delete=models.SET_NULL(), default=None)
    elevator = models.ForeignKey(Elevator, help_text="Лесница", on_delete=models.SET_NULL(), default=None)
    section = models.ForeignKey(Section, help_text="", on_delete=models.SET_NULL(), default=None)

    class Meta:
        ordering = ['number']