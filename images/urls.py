from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<str:slug>', views.image_detail, name='detail'),
    path('delete/<int:id>/', views.image_delete, name='images_delete'),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),
]