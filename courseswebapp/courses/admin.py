from django.contrib import admin
from .models import Field, Specialization, Course, Section, Lecture, LectureMaterial


admin.site.register(Field)
admin.site.register(Specialization)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(LectureMaterial)

