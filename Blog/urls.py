from django.urls import path, include
from . import views

urlpatterns = [
  path('indexx', views.indexx, name='indexx'),
  path('about', views.about, name='about'),
  path('service', views.service, name='service'),
  path('contact', views.contact, name='contact'),
  path('guards', views.guards, name='guards' ),
]