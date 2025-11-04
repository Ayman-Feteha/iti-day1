from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsTeacher, IsStudent, IsTeacherOrStudent, IsTeacherOrStudentReadOnly


class CourseListView(APIView):
    """
    GET: List all courses (teachers and students can view)
    """
    permission_classes = [IsTeacherOrStudent]
    
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({'courses': serializer.data}, status=status.HTTP_200_OK)


class CourseDetailView(APIView):
    """
    GET: Retrieve a specific course by ID (teachers and students can view)
    """
    permission_classes = [IsTeacherOrStudent]
    
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course_data = CourseSerializer(course).data
            course_data['students'] = list(course.students.values('id', 'username', 'email'))
            course_data['teachers'] = list(course.teachers.values('id', 'username', 'email'))
            return Response(course_data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)


class CourseCreateView(APIView):
    """
    POST: Create a new course (only teachers can create)
    """
    permission_classes = [IsTeacher]
    
    def post(self, request):
        data = request.data
        course = Course.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            start_date=data.get('start_date'),
            end_date=data.get('end_date')
        )
        return Response({
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'start_date': course.start_date,
            'end_date': course.end_date
        }, status=status.HTTP_201_CREATED)


class CourseUpdateView(APIView):
    """
    PUT: Full update of a course (only teachers can update)
    """
    permission_classes = [IsTeacher]
    
    def put(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        course.title = data.get('title', course.title)
        course.description = data.get('description', course.description)
        course.start_date = data.get('start_date', course.start_date)
        course.end_date = data.get('end_date', course.end_date)
        course.save()
        
        return Response({
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'start_date': course.start_date,
            'end_date': course.end_date
        }, status=status.HTTP_200_OK)


class CourseDeleteView(APIView):
    """
    DELETE: Delete a course (only teachers can delete)
    """
    permission_classes = [IsTeacher]
    
    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            return Response({'message': 'Course deleted successfully'}, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)


class CoursePartialUpdateView(APIView):
    """
    PATCH: Partial update of a course (only teachers can update)
    """
    permission_classes = [IsTeacher]
    
    def patch(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        if 'title' in data:
            course.title = data['title']
        if 'description' in data:
            course.description = data['description']
        if 'start_date' in data:
            course.start_date = data['start_date']
        if 'end_date' in data:
            course.end_date = data['end_date']
        
        course.save()
        
        return Response({
            'id': course.id,
            'title': course.title,
            'description': course.description,
            'start_date': course.start_date,
            'end_date': course.end_date
        }, status=status.HTTP_200_OK)