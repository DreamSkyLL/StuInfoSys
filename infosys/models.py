from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Class(models.Model):

    class_id = models.CharField(max_length=20, primary_key=True)
    class_name = models.CharField(max_length=30)
    grade = models.CharField(max_length=4)
    major = models.CharField(max_length=20)
    college = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Class")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse("infosys:class_detail", kwargs={"pk": self.pk})
    

class Student(models.Model):

    student_id = models.CharField(max_length=20, primary_key=True)
    student_name = models.CharField(max_length=20)
    student_sex = models.CharField(max_length=2)
    student_birth = models.DateField(null=True)
    student_address = models.CharField(max_length=100)
    student_tel = models.CharField(max_length=20)
    student_qq = models.CharField(max_length=20)
    class_id = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student_name



class Dormitory(models.Model):

    dormitory_id = models.CharField(max_length=20, primary_key=True)
    building_num = models.CharField(max_length=5, null=True, )
    room_num = models.CharField(max_length=4, null=True)
    floor = models.CharField(max_length=2, null=True)
    master = models.OneToOneField('Live', on_delete=models.SET_NULL, null=True)



    class Meta:
        verbose_name = ("Dormitory")
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.building_num) + "-" + str(self.room_num)

    def save(self, *args, **kwargs):
        self.room_num = int(self.dormitory_id[4:9])
        a = ''
        if (self.dormitory_id[2]=='1'):a="GA"
        if (self.dormitory_id[2]=='2'):a="GB"
        if (self.dormitory_id[2]=='3'):a="GC"
        a = a + self.dormitory_id[3:5]
        self.building_num = a
        
        if (self.dormitory_id[5]=='0'):
            self.floor = int(self.dormitory_id[6]) 
        else: 
            self.floor = int(self.dormitory_id[5])
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("infosys:dormitory_detail", kwargs={"pk": self.pk})
    


class Live(models.Model):

    # STATUS_CHOICES = [
    #     ('LI', 'living在住'),
    #     ('RH', 'rent house租房'),
    #     ('TL', 'take leave请假')
    # ]

    live_id = models.CharField(max_length=20, primary_key=True)
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
    dormitory_id = models.ForeignKey(Dormitory, on_delete=models.CASCADE, null=True)
    bed_num = models.CharField(max_length=2, null=True)


    # status = models.CharField()

    class Meta:
        verbose_name = ("Live")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dormitory_id.__str__()


class Event(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # recorder = models.ForeignKey(User)

    class Meta:
        verbose_name = "学生事件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Representative(models.Model):
    position = models.CharField(max_length=20)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    

    class Meta:
        verbose_name = "representative"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
        