from django.shortcuts import render
from .models import MakeCourse

def course_list(request):
    courses = MakeCourse.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

