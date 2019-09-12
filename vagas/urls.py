from django.urls import path

from .views import vagas_list, index

urlpatterns = [
    path("", index, name="index"),
    path("carreiras", vagas_list)
]

