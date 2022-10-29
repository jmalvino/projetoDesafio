from audioop import reverse
from ssl import AlertDescription
from django.shortcuts import render
from .models import Pacientes
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


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
    fields = ['nome','telefone','endereco','numero','cidade','uf','pais','cep']
    template_name: 'pacientes/pacientes_form.html'
    success_message = "Cadastrado com sucesso!!"
    success_url = reverse_lazy('index')
