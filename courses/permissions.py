from rest_framework.permissions import BasePermission
from rest_framework.decorators import permission_classes
from django.http import JsonResponse
from functools import wraps

def role_required(*allowed_roles):
    """
    Decorator to check if user has one of the required roles.
    Usage: @role_required('teacher', 'student')
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Authentication credentials were not provided'}, status=401)
            
            for role in allowed_roles:
                try:
                    getattr(request.user, role)
                    return view_func(request, *args, **kwargs)
                except:
                    pass
            
            return JsonResponse({'error': f'Only users with roles {allowed_roles} can access this'}, status=403)
        
        return wrapper
    return decorator