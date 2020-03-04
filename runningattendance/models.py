from django.db import models
from django.utils import timezone
from infosys.models import Student

class Attendance(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    inspector = models.ForeignKey(Student,related_name='attendance_inspector', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = '考勤'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Takeleave(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    reason = models.CharField(max_length=50)
    inspector = models.ForeignKey(Student,related_name='takeleave_inspector', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "请假"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id

    