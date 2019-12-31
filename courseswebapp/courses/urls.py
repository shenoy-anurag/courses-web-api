from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()

router.register('fields', views.FieldsView)
router.register('specializations', views.SpecializationsView)
router.register('courses', views.CoursesView)
router.register('sections', views.SectionsView)
router.register('lectures', views.LecturesView)

urlpatterns = [
    path('', include(router.urls))
]
