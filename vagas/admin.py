from django.contrib import admin

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
    pass
