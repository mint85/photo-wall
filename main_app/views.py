# from lib2to3.pygram import python_grammar_no_print_statement
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .models import Photo


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

