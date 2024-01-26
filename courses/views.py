from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
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

#view for accesing the course
def course_detail(request, pk):
    course = get_object_or_404(MakeCourse, pk=pk)
    return render(request, 'courses/course_detail.html', {'course':course })