from django.shortcuts import render, redirect
from .models import MakeCourse
from .forms import CourseForm
#view for listing courses
def course_list(request):
    courses = MakeCourse.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

#view for creating courses
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form':form})