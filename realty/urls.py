from django.urls import path, include
from realty import views

urltablelist = [
    path('BuildingType', views.BuildingTypeListView.as_view(), name="BuildingType"),

]

urlpatterns = [
    path('', views.index, name='Home'),
    path('look/',include(urltablelist))
]
