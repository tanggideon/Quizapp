from django.shortcuts import render, redirect
from quiz.models import Quiz
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Student
from reports.models import QuizAttempts

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        
    return render(request, "home/login.html")


def logout(request):
    logout(request)
    return redirect("login")
    



def quizcount():
    quizzes = Quiz.objects.all().count()
    print(quizzes)


# @login_required(login_url="index")
def dashboard(request):
    return render(request, "home/index.html")


def profile(request, pk):
    user = User.objects.get(id=pk)
    student = user.student.all()
    context = {
        "student":student
    }
    return render(request, "home/profile.html", context=context)


def newQuiz(request):
    return render(request, "home/new_quiz.html")

