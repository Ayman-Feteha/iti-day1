from django.shortcuts import render

# Create your views here.
def teacher_list(request):
    return render(request, 'teachers/teacher_list.html')