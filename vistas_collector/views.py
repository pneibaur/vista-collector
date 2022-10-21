from multiprocessing import context
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from vistas_collector.models import Flair, Vista, Comment, User, Photo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CommentForm, FlairForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com'
BUCKET = "catcollector-phil-11"


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def vistas_index(request):
    vistas = Vista.objects.all()
    return render(request, "vistas/index.html", {"vistas": vistas})

@login_required
def user_vistas(request):
    vistas = request.user.vista_set.all()
    return render(request, 'vistas/index.html', {'vistas': vistas})

@login_required
def vista_detail(request, vista_id):
    vista = Vista.objects.get(id=vista_id)
    comment_form = CommentForm()
    flair_form = FlairForm()
    unassociated_tags = Flair.objects.exclude(id__in = vista.tags.all().values_list('id'))
    return render(request, "vistas/detail.html", {
        "vista": vista, 
        "comment_form": comment_form, 
        'flair_form': flair_form, 
        'unassociated_tags': unassociated_tags
        })

@login_required
def add_comment(request, vista_id, user_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.vista_id = vista_id
        new_comment.user_id = user_id
        new_comment.save()
    return redirect("vista_detail", vista_id=vista_id)

@login_required
def remove_comment(request, vista_id, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect("vista_detail", vista_id=vista_id)

@login_required
def add_flair(request, vista_id, user_id):
    form = FlairForm(request.POST)
    if form.is_valid():
        new_flair = form.save(commit=False)
        new_flair.vista_id = vista_id
        new_flair.user_id = user_id
        v = Vista.objects.get(id=vista_id)
        u = User.objects.get(id=user_id)
        f = Flair.objects.create(tag=new_flair, user=u)
        v.tags.add(f)
        v.save()
    return redirect('vista_detail', vista_id=vista_id)

@login_required
def assign_flair(request, vista_id, flair_id):
    Vista.objects.get(id=vista_id).tags.add(flair_id)
    return redirect('vista_detail', vista_id=vista_id)

@login_required
def unassign_flair(request, vista_id, flair_id):
    Vista.objects.get(id=vista_id).tags.remove(flair_id)
    return redirect('vista_detail', vista_id=vista_id)

class VistaCreate(LoginRequiredMixin, CreateView):
    model = Vista
    fields = ["name", "img", "description", "season", "year", "location", "state_province", "country",]
    success_url = "/vistas/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VistaUpdate(LoginRequiredMixin, UpdateView):
    model = Vista
    fields = ["name", "description", "season", "year", "location", "state_province", "country",]


class VistaDelete(LoginRequiredMixin, DeleteView):
    model = Vista
    success_url = "/vistas/"

class FlairList(LoginRequiredMixin, ListView):
    model = Flair
    template_name = 'flairs/index.html'

class FlairDetail(LoginRequiredMixin, DetailView):
    model = Flair
    template_name = 'flairs/detail.html'

class FlairUpdate(LoginRequiredMixin, UpdateView):
    model = Flair
    fields = ['tag',]

class FlairDelete(LoginRequiredMixin, DeleteView):
    model = Flair
    success_url = '/flairs/'


def add_photo(request, vista_id):
    photo_file = request.FILES.get("photo-file", None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique 'key' for s3. needs an image file extension too.
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # this assembles the url string together. 
            url = f"{S3_BASE_URL}/{BUCKET}/{key}"
            # here it's assigned to the vista_id. but you can also assign to the cat object too. 
            photo = Photo(url=url, vista_id=vista_id)
            photo.save()
        except:
            print("An error occurred uploading this file to s3...")
    return redirect('vista_detail', vista_id=vista_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            error_message = "Invalid signup - please try again."
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)