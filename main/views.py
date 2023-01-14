from django.shortcuts import render
from .models import Home, Relevance, Skills, Geography, LastVacancies
from .utils import get_vacancies


# Create your views here.

def home(request):
    homepage = Home.objects.all()[0]
    return render(
        request,
        'main/home.html',
        context={
            'homepage': homepage,
        }
    )


def relevance(request):
    relevancepage = Relevance.objects.all()[0]
    return render(
        request,
        'main/relevance.html',
        context={
            'relevancepage': relevancepage,
        }
    )


def geography(request):
    geographypage = Geography.objects.all()[0]
    return render(
        request,
        'main/geography.html',
        context={
            'geographypage': geographypage,
        }
    )


def skills(request):
    skillspage = Skills.objects.all()[0]
    return render(
        request,
        'main/skills.html',
        context={
            'skillspage': skillspage,
        }
    )


def last_vacancies(request):
    vacanciespage = LastVacancies.objects.all()[0]
    return render(request, 'main/last_vacanvies.html',
                  context={'vacancies': get_vacancies(),
                           'vacanciespage': vacanciespage})
