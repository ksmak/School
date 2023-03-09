# DRF
from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

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
    RegisterSerializer,
    TeacherSerializer,
    StudentSerializer,
    GroupSerializer,
    SubjectSerializer,
    LectureSerializer,
    MarkSerializer,
)
from .permissions import MainPermission


class RegisterView(APIView):
    """Register student view."""
    permission_classes = [AllowAny]

    def post(
        self,
        request: Request,
        *args,
        **kwargs,
    ) -> Response:
        print(request.data)
        serializer = RegisterSerializer(
            data=request.data
        )

        if not serializer.is_valid():
            return Response({
                'error': serializer.errors
            }, status=400)

        serializer.save()

        return Response({
            'result': 'OK',
        }, status=200)


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
