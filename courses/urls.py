from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    CoursePartialUpdateView
)

urlpatterns = [
    path('list', CourseListView.as_view(), name='course-list'),
    path('detail/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('create', CourseCreateView.as_view(), name='course-create'),
    path('update/<int:pk>', CourseUpdateView.as_view(), name='course-update'),
    path('delete/<int:pk>', CourseDeleteView.as_view(), name='course-delete'),
    path('partial-update/<int:pk>', CoursePartialUpdateView.as_view(), name='course-partial-update'),
]
