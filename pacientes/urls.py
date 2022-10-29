from django.urls import path
from . import views
from .views import PacientesCreate


urlpatterns = [
    path('', views.index),
    path('cadastrar', PacientesCreate.as_view(), name="cadastar-pacientes")
]
