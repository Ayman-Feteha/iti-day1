from django.urls import include, path
from .views import login, logout, register_student, register_teacher
urlpatterns = [
    path('login', login),
    path('logout', logout),
    path('register-student', register_student),
    path('register-teacher', register_teacher),
]