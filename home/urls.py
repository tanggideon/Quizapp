from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout/", views.index, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("new-quiz", views.newQuiz, name="newQuiz"),
]