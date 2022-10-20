from django.shortcuts import render, redirect
# from django.http import HttpResponse
from vistas_collector.models import Flair, Vista, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CommentForm, FlairForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def vistas_index(request):
    vistas = Vista.objects.all()
    return render(request, "vistas/index.html", {"vistas": vistas})

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


def add_comment(request, vista_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.vista_id = vista_id
        new_comment.save()
    return redirect("vista_detail", vista_id=vista_id)

def remove_comment(request, vista_id, comment_id):
    Comment.objects.get(id=comment_id).delete()
    return redirect("vista_detail", vista_id=vista_id)

def add_flair(request, vista_id):
    form = FlairForm(request.POST)
    if form.is_valid():
        new_flair = form.save(commit=False)
        new_flair.vista_id = vista_id
        v = Vista.objects.get(id=vista_id)
        f = Flair.objects.create(tag=new_flair)
        v.tags.add(f)
        v.save()
    return redirect('vista_detail', vista_id=vista_id)

def assign_flair(request, vista_id, flair_id):
    Vista.objects.get(id=vista_id).tags.add(flair_id)
    return redirect('vista_detail', vista_id=vista_id)

def unassign_flair(request, vista_id, flair_id):
    Vista.objects.get(id=vista_id).tags.remove(flair_id)
    return redirect('vista_detail', vista_id=vista_id)

class VistaCreate(CreateView):
    model = Vista
    fields = ["name", "img", "description", "season", "year", "location", "state_province", "country",]
    success_url = "/vistas/"


class VistaUpdate(UpdateView):
    model = Vista
    fields = ["name", "description", "season", "year", "location", "state_province", "country",]


class VistaDelete(DeleteView):
    model = Vista
    success_url = "/vistas/"

class FlairList(ListView):
    model = Flair
    template_name = 'flairs/index.html'

class FlairDetail(DetailView):
    model = Flair
    template_name = 'flairs/detail.html'

class FlairUpdate(UpdateView):
    model = Flair
    fields = ['tag',]

class FlairDelete(DeleteView):
    model = Flair
    success_url = '/flairs/'