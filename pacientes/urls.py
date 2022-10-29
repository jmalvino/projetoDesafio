from django.urls import path
from . import views
from .views import PacientesCreate, PacientesList


urlpatterns = [
    path('', views.index, name="index"),
    path('cadastrar', PacientesCreate.as_view(), name="cadastar-pacientes"),
    path('listar', views.index, name="listar-pacientes")
    
]
