from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from .models import Course
from .serializers import CourseSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .permissions import role_required
# Create your views here.

@api_view(['GET'])
@role_required('teacher', 'student')
def course_list(request):
    courses = Course.objects.all()
    return JsonResponse({'courses': list(courses.values())})

@api_view(['GET'])
@role_required('teacher', 'student')
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        course_data = CourseSerializer(course).data
        course_data['students'] = list(course.students.values('id', 'username', 'email'))
        course_data['teachers'] = list(course.teachers.values('id', 'username', 'email'))
        return JsonResponse(course_data)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)

@csrf_exempt
@api_view(['POST'])
@role_required('teacher')
def course_create(request):
    data = request.data
    course = Course.objects.create(
        title=data.get('title'),
        description=data.get('description'),
        start_date=data.get('start_date'),
        end_date=data.get('end_date')
    )
    return JsonResponse({'id': course.id,
                         'title': course.title,
                         'description': course.description,
                         'start_date': course.start_date,
                         'end_date': course.end_date}, status=201)

@api_view(['PUT'])
@role_required('teacher')
def course_update(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    
    data = request.data
    course.title = data.get('title', course.title)
    course.description = data.get('description', course.description)
    course.start_date = data.get('start_date', course.start_date)
    course.end_date = data.get('end_date', course.end_date)
    course.save()
    
    return JsonResponse({'id': course.id,
                         'title': course.title,
                         'description': course.description,
                         'start_date': course.start_date,
                         'end_date': course.end_date}, status=200)

@api_view(['DELETE'])
@role_required('teacher')
def course_delete(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        course.delete()
        return JsonResponse({'message': 'Course deleted successfully'}, status=200)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    
@api_view(['PATCH'])
@role_required('teacher')
def course_partial_update(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    
    data = request.data
    if 'title' in data:
        course.title = data['title']
        course.save()
    if 'description' in data:
        course.description = data['description']
    return JsonResponse({'id': course.id,
                         'title': course.title,
                         'description': course.description}, status=200)