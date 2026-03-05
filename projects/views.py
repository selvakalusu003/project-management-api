from rest_framework import viewsets, generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@api_view(['GET'])
def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@test.com",
            password="admin123"
        )
        return Response({"message": "Admin user created"})
    return Response({"message": "Admin already exists"})