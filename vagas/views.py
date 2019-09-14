from django.shortcuts import render


def vagas_list(request):
    return render(request, "vagas/vaga_list.html")

def index(request):
    return render(request, "pages/index.html")

def candidatura(request):
    pass

# vagas páginas
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

