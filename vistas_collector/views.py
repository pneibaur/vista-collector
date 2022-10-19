from django.shortcuts import render, redirect
# from django.http import HttpResponse
from vistas_collector.models import Flair, Vista
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CommentForm


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
    return render(request, "vistas/detail.html", {"vista": vista, "comment_form": comment_form})


def add_comment(request, vista_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.vista_id = vista_id
        new_comment.save()
    return redirect("vista_detail", vista_id=vista_id)


class VistaCreate(CreateView):
    model = Vista
    fields = "__all__"
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

class FlairCreate(CreateView):
    model = Flair
    fields = ['tag',]

class FlairUpdate(UpdateView):
    model = Flair
    fields = ['tag',]

class FlairDelete(DeleteView):
    model = Flair
    success_url = '/flairs/'