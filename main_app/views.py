from lib2to3.pygram import python_grammar_no_print_statement
from django.shortcuts import render, redirect
from .models import Photo

# Define the home view
def home(request):
    return render(request, 'home.html')

def photos_index(request):
    photos = Photo.objects.all()
    return render(request, 'photos/index.html', { 'photos': photos })

def photos_detail(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    #if photo.user_id != request.user.id:
        #return redirect('photos_index')
    return render(request, 'photos/detail.html', { 'photo': photo }) 