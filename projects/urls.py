from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, RegisterView, create_admin
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Project Management API running"})

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('', home),
    path('create-admin/', create_admin),
]


