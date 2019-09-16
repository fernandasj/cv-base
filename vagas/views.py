from django.shortcuts import render

from .forms import RegisterCandidatura
from .models import Candidatura

# principal
def vagas_list(request):
    return render(request, "vagas/vaga_list.html")

def index(request):
    return render(request, "pages/index.html")

def candidatura(request):
    pass

# vagas
def developer_page(request):
    return render(request, "vagas/developer_page.html")

def designer_page(request):
    return render(request, "vagas/designer_page.html")

def ux_designer_page(request):
    return render(request, "vagas/ux_designer_page.html")

def marketing_page(request):
    return render(request, "vagas/marketing_page.html")

def project_manager_page(request):
    return render(request, "vagas/project_manager_page.html")

# candidatura
def candidatura_page(request):
    if request.method == 'POST':
        print("Entrou 1")

        form = RegisterCandidatura(request.POST)
    
        print("Validando form")
        if form.is_valid():
            print("Form válido 2")
            
            candidatura = form.save(commit=False)

            print(candidatura)

            candidatura.vaga = request.GET.get('vaga')
            candidatura.nome = request.POST['nome'] + " " + request.POST['sobrenome']
            candidatura.email = request.POST['email']
            candidatura.telefone = request.POST['telefone']
            candidatura.experiencia_profissional = request.POST['experiencia_profissional']
            candidatura.experiencia_academica = request.POST['experiencia_academica']
            candidatura.motivacao = request.POST['motivacao']
            
            print("Paasou daqui, já pode comemorar 3")

            candidatura.save()
            
            print("Salvo com a força do ódio 4")

            return render(request, "pages/sucesso.html")
        else:
            form = RegisterCandidatura()
        
    return render(request, "pages/candidatura_vaga.html")