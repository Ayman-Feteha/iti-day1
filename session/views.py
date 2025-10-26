from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from students.models import Student
from teachers.models import Teacher
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login (request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({
            'message': 'Login successful',
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        })
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

@api_view(['POST'])
@permission_classes([AllowAny])
def logout(request):
    auth_logout(request)
    return JsonResponse({'message': 'Logout successful'})

@api_view(['POST'])
@permission_classes([AllowAny])
def register_student(request):
    data = request.data
    user = User.objects.create_user(
        username=data.get('username'),
        password=data.get('password'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        email=data.get('email')
    )
    student = Student.objects.create(
        user=user,
        date_of_birth=data.get('date_of_birth')
    )
    return JsonResponse({'message': 'Student registered successfully'}, status=201)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_teacher(request):
    data = request.data
    user = User.objects.create_user(
        username=data.get('username'),
        password=data.get('password'),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        email=data.get('email')
    )
    teacher = Teacher.objects.create(
        user=user,
        date_of_hire=data.get('date_of_hire')
    )
    return JsonResponse({'message': 'Teacher registered successfully'}, status=201)