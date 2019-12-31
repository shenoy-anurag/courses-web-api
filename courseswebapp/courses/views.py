from django.shortcuts import render
from rest_framework import viewsets
from .models import Field, Specialization, Course, Section, Lecture, LectureMaterial
from .serializers import (FieldSerializer, SpecializationSerializer, CourseSerializer, SectionSerializer,
                          LectureSerializer)


class FieldsView(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class SpecializationsView(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class CoursesView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SectionsView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class LecturesView(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
