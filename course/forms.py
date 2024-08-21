from django import forms
from .models import Course, Student, Teacher, About, Reklama, Comment, Contact, User

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'image', 'context', 'lesson_count', 'educations_form', 'lesson_time', 'category']



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'age', 'image', 'experience']



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'gender', 'category']


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['text', 'image']



class ReklamaForm(forms.ModelForm):
    class Meta:
        model = Reklama
        fields = ['title', 'image', 'context']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'image', 'context']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'context', 'phone', 'comment']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']