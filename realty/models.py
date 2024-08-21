from django.db import models
import uuid

#Справочники
class BuildingType(models.Model):
    """Справочник типов строений"""
    name = models.CharField(max_length=250,help_text="Наименование")
    slug = models.SlugField(max_length=250, unique=True, default=None)
    description = models.CharField(max_length=250, help_text="Описание")

    def __str__(self):
        return self.name


class Countrie(models.Model):
    """Справочник стран"""
    name = models.CharField(max_length=100, help_text="Название страны")
    slug = models.SlugField(max_length=100, unique=True, default=None)
    abbreviations = models.CharField(max_length=4, help_text="Абривиатура")

    def __str__(self):
        return self.name


class RegionCode(models.Model):
    "Справочник код субъектов"
    code = models.CharField(max_length=4, help_text="Код региона")

    def __str__(self):
        return self.code

class Region(models.Model):
    """Справочник субъектов"""
    name = models.CharField(max_length=100, help_text="Название субъекта")
    slug = models.SlugField(max_length=100, unique=True, default=None)
    abbreviations = models.CharField(max_length=10, help_text="Абривиатура", default=None)
    code = models.ForeignKey(RegionCode, on_delete=models.SET_NULL,
                             help_text="Код региона", null=True)

    def __str__(self):
        return self.name



class Locality(models.Model):
    """Справочник начеленных пунктов    """
    name = models.CharField(max_length=250, help_text="Назвение населенного пункта")

    def __str__(self):
        return self.name

class StreetType(models.Model):
    """Справочник типов дорог в населенном пункте. Пример: улица."""
    name = models.CharField(max_length=100, help_text="Тип дороги (улицы) в городе")
    abbreviations = models.CharField(max_length=6, help_text="Абривиатура названия")

    def __str__(self):
        return self.name

class SectionType(models.Model):
    """Справочник типов секций"""
    name = models.CharField(max_length=50, help_text="Наименование секции")

    def __str__(self):
        return self.name

class EntranceType(models.Model):
    """Справочник типов входов"""
    name = models.CharField(max_length=50, help_text="Тип входа (парадная / подъезд)")

    def __str__(self):
        return self.name

class Entrance(models.Model):
    """Справочник входов"""
    entrance_type = models.OneToOneField(EntranceType, on_delete=models.SET_NULL,
                                         help_text="Тип входа", null=True)
    numbers = models.CharField(max_length=10, help_text="Номер входа")
    description = models.TextField(help_text="Описание")

    def __str__(self):
        return f'{self.entrance_type.name} {self.numbers}'

class EntranceSpecial(models.Model):
    """Нестандартных справочников входов"""
    name = models.CharField(max_length=150, help_text="Наименование входа")
    description = models.TextField(help_text="Описание")

    def __str__(self):
        return self.name

class Elevator(models.Model):
    """Справочник лифтов"""
    name = models.CharField(max_length=150, help_text="Название лифта")
    description = models.TextField(help_text="Описание")

    def __str__(self):
        return self.name

class Ladder(models.Model):
    """Справочник лесница"""
    name = models.CharField(max_length=150, help_text="Название лесница")
    description = models.TextField(help_text="Описание")

    def __str__(self):
        return self.name

class FloorSpecial(models.Model):
    name = models.CharField(help_text="Тип этажа")
    description = models.TextField(help_text="Описание этажа")

    def __str__(self):
        return self.name

class SpaceType(models.Model):
    name = models.CharField(max_length=50, help_text="Тип помещения")
    discription = models.TextField(help_text="Описание помещения")

    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=50, help_text="Тип комнаты")
    discription = models.TextField(help_text="Описание комнаты")

    def __str__(self):
        return self.name

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
    country = models.OneToOneField(Countrie, on_delete=models.SET_NULL,
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

    def __str__(self):
        return f'{self.building_type} {self.building_number} {self.street_type} {self.street}'

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

    def __str__(self):
        return f'Секция {self.number}'

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

    def __str__(self):
        return f'Этаж: {self.number}'

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


    def __str__(self):
        return f'Помещение: {self.space_type} {self.number}'

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

    def __str__(self):
        return f"Комната: {self.type.name}"