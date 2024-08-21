import django_tables2 as tables
from . import models

class BuildingTypeTable(tables.Table):
    """
    Таблица: BuildingType
    Отоброжает поля: name, description
    """
    class Meta:
        model = models.BuildingType
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "description")


class CountrieTable(tables.Table):
    """
    Таблица: Countrie
    Отоброжает поля: name, description
    """
    class Meta:
        model = models.Countrie
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "description")