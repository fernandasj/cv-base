from django import forms
from .models import Candidatura

class RegisterCandidatura(forms.ModelForm):

    # vaga = forms.CharField()
    # nome = forms.CharField()
    # email = forms.EmailField()
    # telefone = forms.CharField()
    # experiencia_profissional = forms.CharField()
    # experiencia_academica = forms.CharField()
    # motivacao = forms.CharField()

    class Meta:
        model = Candidatura
        fields = ('nome', 'email','telefone', 'experiencia_profissional', 'experiencia_academica', 'motivacao')