# Django
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Teacher(models.Model):
    """Teacher model."""
    teacher = models.OneToOneField(
        verbose_name='teaher',
        to=User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    def __str__(self) -> str:
        return f"{self.teacher}"


class Student(models.Model):
    """Student model."""
    student = models.OneToOneField(
        verbose_name='student',
        to=User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self) -> str:
        return f"{self.student}"


class Group(models.Model):
    """Group model."""
    name = models.CharField(
        verbose_name='name',
        max_length=100
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='year',
        default=timezone.datetime.now().year
    )
    students = models.ManyToManyField(
        verbose_name='students',
        to=Student,
        related_name='students'
    )
    curator = models.ForeignKey(
        verbose_name='curator',
        to=Teacher,
        on_delete=models.RESTRICT
    )


class Subject(models.Model):
    """Subject model."""
    name = models.CharField(
        verbose_name='name',
        max_length=200
    )
    lecturers = models.ManyToManyField(
        verbose_name='lecturers',
        to=Teacher,
        related_name='lecturers'
    )
    assistants = models.ManyToManyField(
        verbose_name='assistants',
        to=Teacher,
        related_name='assistants',
    )
    groups = models.ManyToManyField(
        verbose_name='groups',
        to=Group,
        related_name='groups',
    )

    class Meta:
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class Lecture(models.Model):
    """Lecturer model."""
    subject = models.ForeignKey(
        verbose_name='subject',
        to=Subject,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='name',
        max_length=200
    )
    description = models.TextField(
        verbose_name='description',
        null=True,
        blank=True
    )
    hours = models.PositiveSmallIntegerField(
        verbose_name='hours',
        default=0
    )
    material = models.FileField(
        verbose_name='material',
        upload_to='materials/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'lecture'
        verbose_name_plural = 'lectures'
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class Mark(models.Model):
    """Mark model."""
    lecture = models.ForeignKey(
        verbose_name='lecture',
        to=Lecture,
        on_delete=models.RESTRICT
    )
    teacher = models.ForeignKey(
        verbose_name='teacher',
        to=Teacher,
        on_delete=models.RESTRICT
    )
    student = models.ForeignKey(
        verbose_name='student',
        to=Student,
        on_delete=models.RESTRICT
    )
    bal = models.PositiveSmallIntegerField(
        verbose_name='bal',
        default=0
    )
    create_date = models.DateTimeField(
        verbose_name='created date',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'mark'
        verbose_name_plural = 'marks'
        ordering = ('create_date', )

    def __str__(self) -> str:
        return (f"teacher:{self.teacher} student:{self.student}"
                f"lecture:{self.lecture} bal:{self.bal}")
