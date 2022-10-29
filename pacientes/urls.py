from django.urls import path
from . import views
from .views import PacientesCreate, PacientesList
from .views import PacientesUpdate

urlpatterns = [
    path('', views.index, name="index"),
    path('cadastrar', PacientesCreate.as_view(), name="cadastar-pacientes"),
    path('listar', PacientesList.as_view(), name="listar-pacientes"),
    path('editar/pacientes/<int:pk>/', PacientesUpdate.as_view(), name="editar-pacientes"),
    
]
