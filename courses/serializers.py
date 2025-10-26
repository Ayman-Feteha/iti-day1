from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'start_date', 'end_date']

