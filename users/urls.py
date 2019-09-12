from django.urls import path

from .views import users_login

from django.views.generic.base import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url='login', permanent=False), name='index'),
    path("login", users_login)
]

