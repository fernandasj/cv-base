from django import forms
from .models import Candidatura

class RegisterCandidatura(forms.ModelForm):

    class Meta:
        model = Candidatura
        fields = ('nome', 'email','telefone', 'experiencia_profissional', 'experiencia_academica', 'motivacao')