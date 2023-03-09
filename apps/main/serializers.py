# Python
from typing import Optional

# DRF
from rest_framework import serializers

# Django
from django.contrib.auth import get_user_model

# Project
from .models import (
    Teacher,
    Student,
    Group,
    Subject,
    Lecture,
    Mark
)
from auths.serializers import CustomUserSerializer


User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    """Serializer for registrate teacher"""
    STATUS_STUDENT = 1
    STATUS_TEACHER = 2
    STATUSES = (
        (STATUS_STUDENT, 'Student'),
        (STATUS_TEACHER, 'Teacher'),
    )
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    patronymic = serializers.CharField(required=False, max_length=150)
    status = serializers.ChoiceField(STATUSES)

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email']).first()
        if user:
            raise serializers.ValidationError("User is exists.")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            patronymic=validated_data['patronymic']
        )
        obj: Optional[Student | Teacher]
        if validated_data['status'] == self.STATUS_STUDENT:
            obj = Student.objects.create(
                student=user
            )
        elif validated_data['status'] == self.STATUS_TEACHER:
            obj = Teacher.objects.create(
                teacher=user
            )
        else:
            raise serializers.ValidationError("Status is invalid.")
        return obj


class TeacherSerializer(serializers.ModelSerializer):
    """Teacher serializer."""
    teacher = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = (
            'teacher',
        )


class StudentSerializer(serializers.ModelSerializer):
    """Teacher serializer."""
    student = CustomUserSerializer()

    class Meta:
        model = Student
        fields = (
            'student',
        )


class GroupSerializer(serializers.ModelSerializer):
    """Group serializer."""
    class Meta:
        model = Group
        fields = (
            'name',
            'year',
            'students',
            'curator',
        )


class SubjectSerializer(serializers.ModelSerializer):
    """Subject serializer."""
    id = serializers.ReadOnlyField()

    class Meta:
        model = Subject
        fields = (
            "id",
            'name',
            'lecturers',
            'assistants',
            'groups',
        )


class LectureSerializer(serializers.ModelSerializer):
    """Lecture serializer."""
    class Meta:
        model = Lecture
        fields = (
            'subject',
            'name',
            'description',
            'hours',
            'material'
        )


class MarkSerializer(serializers.ModelSerializer):
    """Mart serializer."""
    lecture = CustomUserSerializer()
    teacher = CustomUserSerializer()
    Student = CustomUserSerializer()
    class Meta:
        model = Mark
        fields = (
            'lecture',
            'teacher',
            'student',
            'bal',
            'create_date'
        )
