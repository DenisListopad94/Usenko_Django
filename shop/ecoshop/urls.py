from django.urls import path, re_path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("info/<str:ecoshop>/<slug:street>/<int:number>/", views.info_ecoshop, name="info_ecoshop"),
    re_path(r"^regular/(?P<year>[12][09][89012][0-9])/?$", views.regular_views),
    path("data/", views.data_views, name="data_views"),
]
