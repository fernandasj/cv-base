from django.shortcuts import render


def vagas_list(request):
    return render(request, "vagas/vaga_list.html")
