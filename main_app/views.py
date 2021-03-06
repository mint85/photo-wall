# from lib2to3.pygram import python_grammar_no_print_statement
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .models import Photo, PhotoFile
from django.contrib.auth.models import User
import boto3
import uuid

# Environment Variables for S3
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'photo-wall-persistence-amj'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('photos_index')
        else:
            error_message = 'Invalid Credentials - Please Try Again'
    form = UserCreationForm()
    context = { 'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def example(request):
    photos = Photo.objects.filter(user=1)
    return render(request, 'example.html', {'photos': photos })

def example_detail(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    return render(request, 'example_detail.html', { 'photo': photo }) 

@login_required
def photos_index(request):
    photos = Photo.objects.filter(user=request.user)
    return render(request, 'photos/index.html', { 'photos': photos })

@login_required
def photos_detail(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    #if photo.user_id != request.user.id:
        #return redirect('photos_index')
    return render(request, 'photos/detail.html', { 'photo': photo }) 

class PhotoCreate(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ('name', 'description')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_absolute_url(self):
    #     return reverse('photos_index')

class PhotoUpdate(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ('name', 'description')

class PhotoDelete(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/photos/'

@login_required
def add_photo(request, photo_id):
        photo_file = request.FILES.get('photo-file', None)
        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
            try:
                s3.upload_fileobj(photo_file, BUCKET, key)
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                photo = PhotoFile(url=url, photo_id=photo_id)
                photo.save()
            except Exception as error:
                print('**************')
                print('An error occurred uploading file to S3')
                print(error)
                print('**************')
        return redirect('photo_detail', photo_id=photo_id)
