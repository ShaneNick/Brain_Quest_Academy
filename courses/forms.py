from django import forms
from .models import MakeCourse

class CourseForm(forms.ModelForm):
    class Meta:
        model = MakeCourse
        fields = ['title', 'course_desc']