from django.shortcuts import render

# Create your views here.
def performance(request):
    return render(request, "performance/performance.html")