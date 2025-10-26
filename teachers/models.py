from django.db import models
from courses.models import Course
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='teacher')
    courses_taught = models.ManyToManyField(Course, related_name='teachers')
    date_of_hire = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"