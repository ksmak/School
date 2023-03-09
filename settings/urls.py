# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# DRF
from rest_framework.routers import SimpleRouter

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Project
from main.views import (
    RegisterView,
    TeacherView,
    StudentView,
    GroupView,
    SubjectView,
    LectureView,
    MarkView,
)

router = SimpleRouter(
    trailing_slash = True
)
router.register(r'teachers', TeacherView)
router.register(r'students', StudentView)
router.register(r'groups', GroupView)
router.register(r'subjects', SubjectView)
router.register(r'lectures', LectureView)
router.register(r'marks', MarkView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view()),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]