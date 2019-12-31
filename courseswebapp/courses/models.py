from django.db import models


class Field(models.Model):
    field = models.CharField(max_length=100)

    def __str__(self):
        return self.field


class Specialization(models.Model):
    field = models.ManyToManyField(Field)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.specialization


class Course(models.Model):
    specialization = models.ManyToManyField(Specialization)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.title


class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class LectureMaterial(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    extra_reading = models.CharField(max_length=100, blank=True)
    code_link = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.extra_reading or self.code_link or self.notes
