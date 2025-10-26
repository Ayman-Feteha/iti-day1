from django.shortcuts import render

# Create your views here.
def student_list(request):
    return render(request, 'students/student_list.html')