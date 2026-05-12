from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tache

class TacheListView(ListView):
    model = Tache
    template_name = 'catalogue/liste.html'
    context_object_name = 'taches'

class TacheCreateView(CreateView):
    model = Tache
    fields = ['titre', 'description', 'terminee']
    template_name = 'catalogue/form.html'
    success_url = reverse_lazy('liste')

class TacheUpdateView(UpdateView):
    model = Tache
    fields = ['titre', 'description', 'terminee']
    template_name = 'catalogue/form.html'
    success_url = reverse_lazy('liste')

class TacheDeleteView(DeleteView):
    model = Tache
    template_name = 'catalogue/confirmer_suppression.html'
    success_url = reverse_lazy('liste')