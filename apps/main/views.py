# DRF
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

# Project
from .models import (
    Teacher,
    Student,
    Group,
    Subject,
    Lecture,
    Mark,
)
from .serializers import (
    TeacherSerializer,
    StudentSerializer,
    GroupSerializer,
    SubjectSerializer,
    LectureSerializer,
    MarkSerializer,
)
from .permissions import MainPermission


class TeacherView(viewsets.ModelViewSet):
    """Teacher viewset."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class StudentView(viewsets.ModelViewSet):
    """Student viewset."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class GroupView(viewsets.ModelViewSet):
    """Group viewset."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [MainPermission]


class LectureView(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated, MainPermission]


class MarkView(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer
    permission_classes = [IsAuthenticated, MainPermission]
