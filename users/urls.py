from django.urls import path

from .views import users_login, dashboard

from django.views.generic.base import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url='login?next=user', permanent=False), name='index')
]

