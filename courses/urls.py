from django.urls import include, path
from .views import course_delete, course_detail, course_list, course_create, course_partial_update, course_update
urlpatterns = [
    path('list', course_list),
    path('detail/<int:pk>', course_detail),
    path('create', course_create),
    path('update/<int:pk>', course_update),
    path('delete/<int:pk>', course_delete),
    path('partial-update/<int:pk>', course_partial_update),
]
