from django.urls import path

from . import views

app_name = 'plant'

urlpatterns = [
    path('', views.index, name='plant_index'),
    path('create/', views.create_plant, name='plant_create'),
    path('edit/<int:plant_id>', views.edit_plant, name='edit_plant'),
    path('show/<str:name>/', views.detail, name='plant_detail'),
    path('id/<int:plant_id>/start', views.start_plant_simulation, name='plant_start'),
    path('id/<int:plant_id>/stop', views.stop_plant_simulation, name='plant_stop'),
    path('delete/<str:plant_id>', views.delete_plant, name='plant_delete'),
]

