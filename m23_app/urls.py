from django.urls import path
from . import views

app_name = 'm23_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_order', views.new_order, name='new_order'),
    path('services', views.services, name='services'),
    path('info', views.info, name='info'),
    path('contacts', views.contacts, name='contacts'),
]
