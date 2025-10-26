from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    """
    Custom permission to only allow teachers to create/update courses.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        try:
            # Check if user has a teacher profile
            request.user.teacher
            return True
        except:
            return False

class IsTeacherOrStudentReadOnly(BasePermission):
    """
    Custom permission to allow teachers full access and students read-only access.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Check if user is a teacher or student
        try:
            # If user is a teacher, allow all actions
            request.user.teacher
            return True
        except:
            pass
        
        try:
            # If user is a student, only allow read operations (GET)
            request.user.student
            return request.method in ['GET','POST']
        except:
            return False