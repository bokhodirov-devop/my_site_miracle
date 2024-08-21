
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import TeacherForm, StudentForm, ContactForm
from .models import Teacher, Student, About, Reklama, Comment, User

from .models import Course


def index(request):
    return render(request, 'index.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'front/project.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'front/project_detail.html', {'course': course})





# List view for teachers
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'
    context_object_name = 'teachers'


# Detail view for a single teacher


########## Student
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Детали студента
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

# Создание нового студента
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Переадресация на список студентов после успешного создания
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# Обновление информации о студенте
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)  # Переадресация на страницу с деталями после обновления
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# Удаление студента
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  # Переадресация на список студентов после удаления
    return render(request, 'students/student_confirm_delete.html', {'student': student})


#About
def about_list(request):
    abouts = About.objects.all()
    return render(request, 'about/about_list.html', {'abouts': abouts})

def about_detail(request, pk):
    about = get_object_or_404(About, pk=pk)
    return render(request, 'about/about_detail.html', {'about': about})



def reklama_list(request):
    reklamas = Reklama.objects.all()
    return render(request, 'myapp/reklama_list.html', {'reklamas': reklamas})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'myapp/comment_list.html', {'comments': comments})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact_form.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    return render(request, 'myapp/user_list.html', {'users': users})

# Add more views as needed
