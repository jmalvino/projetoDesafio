from audioop import reverse
from ssl import AlertDescription
from django.shortcuts import render
from .models import Pacientes
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

# Criacao
class PacientesCreate(CreateView):
    model = Pacientes
    fields = ['nome','telefone','endereco','numero','cidade','uf','pais','cep']
    template_name: 'pacientes/pacientes_form.html'
    success_message = "Cadastrado com sucesso!!"
    success_url = reverse_lazy('index')

def index(request):
    pacientes = Pacientes.objects.all()
    return render (request, 'pacientes/index.html', {'pacientes':pacientes})


class PacientesList(CreateView):
    model = Pacientes
    fields = ['nome']
    template_name: 'pacientes/pacientes_form.html'
    success_message = "Cadastrado com sucesso!!"
    success_url = reverse_lazy('index')

# update
class PacientesUpdate(UpdateView):
    model = Pacientes
    fields = ['nome','telefone','endereco','numero','cidade','uf','pais','cep']
    template_name: 'pacientes/pacientes_form.html'
    success_url = reverse_lazy('index')
