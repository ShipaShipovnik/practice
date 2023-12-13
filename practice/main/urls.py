from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about,name = 'about'),
    path('service', views.service,name = 'service'),
    path('add', views.add,name = 'add'),
]