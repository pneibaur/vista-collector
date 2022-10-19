from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("vistas/", views.vistas_index, name="index"),
    path("vistas/<int:vista_id>", views.vista_detail, name="vista_detail"),
    path("vistas/create/", views.VistaCreate.as_view(), name="vista_create"),
    path("vistas/<int:pk>/update/", views.VistaUpdate.as_view(), name="vista_update"),
    path("vistas/<int:pk>/delete/", views.VistaDelete.as_view(), name="vista_delete"),
    path("vistas/<int:vista_id>/add_comment/", views.add_comment, name="add_comment")
]
