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
    code = models.ForeignKey(RegionCode, on_delete=models.SET_NULL,
                             help_text="Код региона", null=True)


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
    entrance_type = models.OneToOneField(EntranceType, on_delete=models.SET_NULL,
                                         help_text="Тип входа", null=True)
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


class FloorSpecial(models.Model):
    name = models.CharField(help_text="Тип этажа")
    description = models.TextField(help_text="Описание этажа")


class SpaceType(models.Model):
    name = models.CharField(max_length=50, help_text="Тип помещения")
    discription = models.TextField(help_text="Описание помещения")


class RoomType(models.Model):
    name = models.CharField(max_length=50, help_text="Тип комнаты")
    discription = models.TextField(help_text="Описание комнаты")


#Модели
class Building(models.Model):
    """
    Здание
    - Адрес
    - Тип строения
    - Этажность
    - Площадь
    - Описание
    """
    #Base
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Adress
    index = models.CharField(max_length=10, help_text="Индекс")
    country = models.OneToOneField(Сountrie, on_delete=models.SET_NULL,
                                   help_text="Страна", null=True)
    region = models.OneToOneField(Region, on_delete=models.SET_NULL,
                                  help_text="Субъект", null=True)
    locality = models.OneToOneField(Locality, on_delete=models.SET_NULL,
                                    help_text="Начеленный пункт", null=True)
    street_type = models.OneToOneField(StreetType, on_delete=models.SET_NULL,
                                       help_text="Тип дороги", null=True)
    street = models.CharField(max_length=250, help_text="Название дороги (улицы)")

    building_number = models.CharField(max_length=10, help_text="Номер сроения")

    #Common

    building_type = models.OneToOneField(BuildingType, on_delete=models.SET_NULL,
                                         help_text="Тип строения", null=True)
    total_space = models.IntegerField(help_text="Этажность")
    total_square = models.FloatField(help_text="Общая площадь")
    description = models.CharField(help_text="Описание")


    class Meta:
        ordering = ["-created"]

class Section(models.Model):
    """Секция дома."""
    #Base
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Common
    number = models.IntegerField(help_text="Номер секции")
    section_type = models.OneToOneField(SectionType, on_delete=models.SET_NULL,
                                        help_text="Тип секции", null=True)
    entrance_special = models.ForeignKey(EntranceSpecial, on_delete=models.SET_NULL,
                                         help_text="Дополнительный вход", null=True)
    description = models.TextField(help_text="Описание секции")
    building = models.ForeignKey(Building, on_delete=models.SET_NULL,
                                 help_text="Дом", null=True)
    max_number_of_floors = models.IntegerField(help_text="Этажность")

    class Meta:
        ordering = ['number']

class Floor(models.Model):
    """Этаж"""
    #Base
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Entering
    number = models.IntegerField(help_text="Номер этажа")
    ladder = models.ForeignKey(Ladder, help_text="Лифт", on_delete=models.SET_NULL,
                               default=None, null=True)
    elevator = models.ForeignKey(Elevator, help_text="Лесница",
                                 on_delete=models.SET_NULL, default=None, null=True)
    section = models.ForeignKey(Section, help_text="", on_delete=models.SET_NULL,
                                default=None, null=True)

    #Common
    total_space = models.FloatField(help_text="Площадь квартир на эьаже")
    total_square = models.FloatField(help_text="Площадь всего этажа")
    common_area = models.FloatField(help_text="Плащадь общих помещений")
    min_numbre_space = models.CharField(max_length=10, help_text="Номер первой квартиры на этаже")
    max_numbre_space = models.CharField(max_length=10, help_text="Номер последний квартиры на этаже")
    description = models.TextField(help_text="Описание этажа")
    floor_special = models.OneToOneField(FloorSpecial, on_delete=models.SET_NULL, default=None,
                                         help_text="Тип этажа", null=True)

    class Meta:
        ordering = ['number']

class Space(models.Model):
    """Помещение"""
    #Base
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Common
    space_type = models.OneToOneField(SpaceType, on_delete=models.SET_NULL, default=None, null=True)
    number = models.CharField(max_length=10, help_text="Номер квартиры")
    square = models.FloatField(help_text="Площадь квартиры")
    description = models.TextField(help_text="Описание квартиры")

    class Meta:
        ordering = ['number']

class Room(models.Model):
    """Комнаты помещения"""
    #Base
    id = models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Common
    type = models.OneToOneField(RoomType, on_delete=models.SET_NULL,
                                help_text="Тип комнаты помещения", null=True)
    description = models.TextField(help_text="Описание комнаты")
    space = models.ForeignKey(Space, on_delete=models.SET_NULL, default=None,
                              help_text="Помещение", null=True)



