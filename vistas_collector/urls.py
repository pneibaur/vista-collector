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
    path("vistas/<int:vista_id>/add_comment/", views.add_comment, name="add_comment"),
    path("flairs/", views.FlairList.as_view(), name="flair_index"), 
    path("flairs/<int:pk>", views.FlairDetail.as_view(), name="flair_detail"),
    path("flairs/<int:pk>/update", views.FlairUpdate.as_view(), name="flair_update"),
    path("flairs/<int:pk>/delete", views.FlairDelete.as_view(), name="flair_delete"),
    path("vistas/<int:vista_id>/add_flair/", views.add_flair, name="add_flair"),
    path("vistas/<int:vista_id>/assign_flair/<int:flair_id>", views.assign_flair, name='assign_flair'),
    path("vistas/<int:vista_id>/usassign_flair/<int:flair_id>", views.unassign_flair, name='unassign_flair'),
    path("vistas/<int:vista_id>/remove_comment/<int:comment_id>", views.remove_comment, name='remove_comment')
]
