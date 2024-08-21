from django.contrib import admin

from .models import Course, Category, Teacher

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Teacher)