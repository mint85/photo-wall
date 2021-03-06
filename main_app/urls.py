from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('example/', views.example, name='example'),
    path('example/<int:photo_id>/', views.example_detail, name='example_detail'),
    path('photos/', views.photos_index, name='photos_index'),
    path('photos/<int:photo_id>/', views.photos_detail, name='photo_detail'),
    path('photos/create/', views.PhotoCreate.as_view(), name='photos_create'),
    path('photos/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photos_update'),
    path('photos/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photos_delete'),
    path('photos/<int:photo_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name='signup'),
]