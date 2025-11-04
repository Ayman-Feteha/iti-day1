from rest_framework.permissions import BasePermission


class IsTeacher(BasePermission):
    """
    Custom permission to only allow teachers to access the view.
    """
    message = "Only teachers can perform this action."
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        try:
            request.user.teacher
            return True
        except:
            return False


class IsStudent(BasePermission):
    """
    Custom permission to only allow students to access the view.
    """
    message = "Only students can perform this action."
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        try:
            request.user.student
            return True
        except:
            return False


class IsTeacherOrStudent(BasePermission):
    """
    Custom permission to allow both teachers and students to access the view.
    """
    message = "Only teachers or students can perform this action."
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        try:
            request.user.teacher
            return True
        except:
            pass
        
        try:
            request.user.student
            return True
        except:
            return False


class IsTeacherOrStudentReadOnly(BasePermission):
    """
    Custom permission to allow teachers full access and students read-only access.
    """
    message = "You do not have permission to perform this action."
    
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        # Teachers have full access
        try:
            request.user.teacher
            return True
        except:
            pass
        
        # Students only have read access
        try:
            request.user.student
            return request.method in ['GET', 'HEAD', 'OPTIONS']
        except:
            return False