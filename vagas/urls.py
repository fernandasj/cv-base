from django.urls import path

from .views import vagas_list

urlpatterns = [path("", vagas_list)]
