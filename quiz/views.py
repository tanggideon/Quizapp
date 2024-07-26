from django.http import Http404
from django.shortcuts import render
from home.models import Course
from .models import Quiz, Question, Answer
from reports.models import QuizAttempts
from django.contrib.auth.models import User

# Create your views here.
def quizzes(request):
    # Implement Search
    quizs = Quiz.objects.all()
    courses = Course.objects.all()
    questions = Question.objects.all()
    context = {'courses':courses, 'quizzes':quizs, 'questions':questions}
    return render(request, "quiz/quizzes.html", context=context)

def quiz(request, pk):
    try:
        quiz = Quiz.objects.get(id=pk)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")
    
    instructions = quiz.quizinstruction.all()
    questions = quiz.quizquestions.all()
    answers = Answer.objects.all()
    context = { 'quiz':quiz, 'instructions':instructions, 'questions':questions, 'answers':answers }

    if request.method == "POST":
        total_marks = 0
        marks_scored = 0
        choices = []
        passed = False
        for question in questions:
            attempted_answer = request.POST.get(str(question.id))
            try:
                answer = Answer.objects.get(pk=attempted_answer)
                correct_answer = Answer.objects.get(pk=attempted_answer).is_correct
            except Answer.DoesNotExist:
                raise Http404("Answer does not exist")
            total_marks += answer.question.mark
            if correct_answer:
                marks_scored += answer.question.mark
            
            choices.append(attempted_answer)

        if (marks_scored/total_marks) > 0.5:
            passed = True
        else:
            passed = False

        student_attempt = QuizAttempts(student=User.student.objects.get(pk=request.user.id), 
                                       quiz=quiz.id, 
                                       choices=choices, 
                                       score=marks_scored, 
                                       total_marks=total_marks, 
                                       passed=passed)
        print(student_attempt.id)
        exit()
        student_attempt.save()
        print(marks_scored)
        print(total_marks)
        print(choices)
        print(passed)
        
    return render(request, "quiz/quiz.html", context=context)

def success(request):
    return render(request, "quiz/success.html")