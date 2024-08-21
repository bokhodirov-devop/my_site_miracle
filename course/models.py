
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    context = models.TextField()
    lesson_count = models.PositiveIntegerField()
    educations_form = models.CharField(max_length=100)
    lesson_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name




# Teacher
class Teacher(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    experience = models.CharField(max_length=100)
    category = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teachers')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")

    def str(self):
        return self.name


# Student.
class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    category = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male")


    def str(self):
        return self.name


# About
class About(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]


class Reklama(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    context = models.TextField()  # Используем TextField для больших объемов текста
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:50]  # Исправляем на title, так как поля 'text' нет

class Comment(models.Model):
    title = models.CharField(max_length=200)  # Добавляем max_length для CharField
    image = models.ImageField(upload_to='images/')
    context = models.TextField()  # Используем TextField для больших объемов текста
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:50]  # Добавляем метод __str__ для представления объекта

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()  # Используем EmailField для валидации email-адресов
    context = models.TextField()  # Используем TextField для больших объемов текста
    phone = models.CharField(max_length=15)  # Используем CharField для телефонов
    comment = models.TextField()  # Используем TextField для больших объемов текста

    def __str__(self):
        return self.name[:50]  # Исправляем на name, так как поля 'text' нет

class User(models.Model):
    last_name = models.CharField(max_length=200)  # Добавляем max_length для CharField
    first_name = models.CharField(max_length=200)  # Добавляем max_length для CharField

    def __str__(self):
        return f"{self.first_name} {self.last_name}"