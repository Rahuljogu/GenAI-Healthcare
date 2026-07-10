from django.urls import path
from . import views

urlpatterns = [
    path('symptom-checker/', views.symptom_checker_view, name='symptom_checker'),
    path('drug-info/', views.drug_info_view, name='drug_info'),
]
