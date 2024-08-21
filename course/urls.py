
from django.urls import path

from course.views import *

# from .views import course_list, course_detail, index, TeacherListView, \
#     student_list, student_detail, student_create, student_update, student_delete




urlpatterns = [
    path('', index, name='index'),
    path('course_list/', course_list, name='course_list'),
    path('courses/<int:pk>/', course_detail, name='project_detail'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list'),
    path('student', student_list, name='student_list'),
    path('student/<int:pk>/', student_detail, name='student_detail'),
    path('student/new/', student_create, name='student_create'),
    path('student/<int:pk>/edit/', student_update, name='student_update'),
    path('student/<int:pk>/delete/', student_delete, name='student_delete'),
    path('reklama/', reklama_list, name='reklama_list'),
    path('comment/', comment_list, name='comment_list'),
    path('contact/', contact_create, name='contact_create'),
    path('users/', user_list, name='user_list'),
]
