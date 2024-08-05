from django.urls import path, include


from realty import views

urlpatterns = [
    path('', views.index, name='Home'),
]
