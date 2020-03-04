from django.db import models
from django.utils import timezone
from infosys.models import Dormitory, Student

class Check(models.Model):

    dormitory_id = models.ForeignKey(Dormitory, on_delete=models.DO_NOTHING)
    check_time = models.DateTimeField(auto_now=True)
    check_student_id = models.ManyToManyField(Student)
    score = models.SmallIntegerField()
    problem = models.CharField(max_length=50)

    class Meta:

        verbose_name = ("Check")
        verbose_name_plural = verbose_name

    __str__(self):
        return self.id
    