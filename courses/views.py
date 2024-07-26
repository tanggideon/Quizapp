from django.shortcuts import render
from .models import Resource
from home.models import Course
from django.http import Http404
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def courses(request):
    resources = Resource.objects.all()
    courses = Course.objects.all()
    context = {'resources': resources, "courses":courses}
    return render(request, "courses/courses.html", context=context) 


def resources(request):
    resources = Resource.objects.all()
    courses = Course.objects.all()
    if request.method == "POST" and request.FILES['file']:
        try:
            course = Course.objects.get(course_code=request.POST.get("course"))
        except Course.DoesNotExist:
            raise Http404("Course does not exist")
        title = request.POST.get("title")
        description= request.POST.get("description")

        # File Upload Handling
        file = request.FILES['file']
        fs = FileSystemStorage(location='files')
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        # Upload file details to Resource Table in database
        resource = Resource.objects.create(
            course = course,
            title = title,
            description = description,
            resource = uploaded_file_url
        )
        resource.save()

    context = {'resources': resources, "courses":courses}
    return render(request, "courses/resources.html", context=context) 