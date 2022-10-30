from django.urls import path,include
from . import views
from .views import MedicosCreate, MedicosDelete, MedicosList
from .views import MedicosUpdate
from .views import MedicosList


urlpatterns = [    
    path('index', views.index, name="index"),
    path('cadastrar', MedicosCreate.as_view(), name="cadastar-medicos"),
    path('listar', MedicosList.as_view(), name="listar-medicos"),
    path('editar/medicos/<int:pk>/', MedicosUpdate.as_view(), name="editar-medicos"),
    path('excluir/medicos/<int:pk>/', MedicosDelete.as_view(), name="excluir-medicos"),
    
    
]
