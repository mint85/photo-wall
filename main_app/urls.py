from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photos/', views.photos_index, name='photos_index'),
    path('photos/<int:photo_id>/', views.photos_detail, name='photo_detail'),
]