from django.urls import path

from .views import vagas_list, index, developer_page, ux_designer_page, marketing_page, project_manager_page, designer_page, candidatura_page

urlpatterns = [
    path("", index, name="index"),
    path("carreiras", vagas_list),
    path("carreiras/developer", developer_page),
    path("carreiras/ux-designer", ux_designer_page),
    path("carreiras/marketing", marketing_page),
    path("carreiras/project-manager", project_manager_page),
    path("carreiras/designer", designer_page),
    path("carreiras/candidatar/", candidatura_page)
]

