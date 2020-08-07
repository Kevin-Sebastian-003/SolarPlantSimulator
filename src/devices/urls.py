from django.urls import path

from . import views

app_name = 'devices'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_device, name='device_create'),
    path('show/<str:name>/', views.detail, name='device_detail'),
    path('start/<str:name>/', views.start_device, name='device_start'),
    path('stop/<str:name>/', views.stop_device, name='device_stop'),
    path('edit/<str:name>/', views.edit_device, name='device_edit'),
    path('delete/<str:name>/', views.delete_device, name='device_delete'),
]

