from django.urls import path

from . import views

urlpatterns = [
    path("df/", views.indexDF, name="indexDF"),
    path("hf/", views.indexHF, name="indexHF"),
    path("hf/artist-songs", views.HFresultsAN, name="results"),
    path("hf/artist-list", views.HFresultsAP, name="results"),
]
