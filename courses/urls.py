from django.urls import path
from . import views

urlpatterns = [
    path("", views.courses, name="courses"),
    path("resources", views.resources, name="resources"),
]