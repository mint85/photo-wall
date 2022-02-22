# from lib2to3.pygram import python_grammar_no_print_statement
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class PhotoCreate(CreateView):
    model = Photo
    fields = ('name', 'description')

    def get_absolute_url(self):
        return reverse('photos_index')

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ('name', 'description')

class PhotoDelete(DeleteView):
    model = Photo
    success_url = '/photos/'

