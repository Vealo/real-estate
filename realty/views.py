from django.shortcuts import render
from django_tables2 import SingleTableView

from . import models
from . import tables

# Create your views here.
def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python!"}
    return render(request, "main/index.html", context=data)


class BuildingTypeListView(SingleTableView):
    model = models.BuildingType
    table_class = tables.BuildingTypeTable
    template_name = 'realty/buildingType.html'

class CountrieListView(SingleTableView):
    model = models.Countrie
    table_class = tables.CountrieTable
    template_name = 'realty/buildingType.html'
