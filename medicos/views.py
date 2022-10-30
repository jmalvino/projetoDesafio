from audioop import reverse
from ssl import AlertDescription
from django.shortcuts import render
from .models import Medicos
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

# Criacao
class MedicosCreate(CreateView):
    model = Medicos
    fields = ['nome','email','senha']
    template_name: 'medicos/medicos_form.html'
    success_message = "Cadastrado com sucesso!!"
    success_url = reverse_lazy('listar-medicos')

def index(request):
    medicos = Medicos.objects.all()
    return render (request, 'medicos/index.html', {'medicos':medicos})


class MedicosList(CreateView):
    model = Medicos
    fields = ['nome']
    template_name: 'medicos/medicos_form.html'
    success_message = "Cadastrado com sucesso!!"
    success_url = reverse_lazy('listar-medicos')

# update
class MedicosUpdate(UpdateView):
    model = Medicos
    fields = ['nome','email','senha']
    template_name: 'medicos/medicos_form.html'
    success_url = reverse_lazy('listar-medicos')

# delete
class MedicosDelete(DeleteView):
    model = Medicos   
    template_name: 'medicos/form_excluir.html'
    success_url = reverse_lazy('listar-medicos')

# listar
class MedicosList(ListView):
    model = Medicos
    template_name: 'lista.html'
