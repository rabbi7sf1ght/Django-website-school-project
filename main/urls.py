from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('relevance', views.relevance, name='relevance'),
    path('geography', views.geography, name='geography'),
    path('last_vacancies', views.last_vacancies, name='last_vacancies'),
    path('skills', views.skills, name='skills'),
]
