from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course_list, name = 'course_list'),
    path('create/', views.create_course, name = 'create_course'),
    path('course/<int:pk>/', views.course_detail, name = 'course_detail'),
]