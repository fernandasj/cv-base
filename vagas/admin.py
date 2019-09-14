from django.contrib import admin
# from django.contrib.auth.admin import Vaga
from .models import Beneficio, Requisito, Vaga, Candidatura


# @admin.register(Vaga)
# class VagaAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Requisito)
# class RequisitoAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Beneficio)
# class BeneficioAdmin(admin.ModelAdmin):
#     pass


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('vaga','nome', 'email', 'telefone')
    search_fields = ('vaga', 'nome')
    ordering = ("vaga", "nome")

    filter_horizontal = ()
    list_filter = (['vaga'])
    fieldsets = ()