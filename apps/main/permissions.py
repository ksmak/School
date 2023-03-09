# Python
from typing import Any

# DRF
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

# Project
from .models import Teacher, Student


class MainPermission(BasePermission):
    """MainPermission."""
    def has_permission(
        self,
        request: Request,
        view: Any
    ) -> bool:
        user: bool = (
            request.user and request.user.is_active
        )
        student: bool = (
            user and Student.objects.filter(student=request.user).count() == 1
        )
        teacher: bool = (
            user and Teacher.objects.filter(teacher=request.user).count() == 1
        )
        superuser: bool = user and (
            request.user.is_staff and
            request.user.is_superuser
        )
        if view.action in (
            'list',
            'retrieve',
        ):
            return student or teacher or superuser

        if view.action in (
            'create',
            'update',
            'partial_update',
        ):
            return teacher or superuser

        if view.action in (
            'destroy',
        ):
            return superuser
