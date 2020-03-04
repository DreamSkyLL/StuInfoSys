from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from .forms import AttendanceForm
from infosys.models import Student, Class
from .models import Attendance, Takeleave

class ResultView(ListView):
  def get(self, request, *args, **kwargs):
    date = self.request.GET.get('date')
    grade = self.request.GET.get('grade')
    if grade:
      classes = Class.objects.filter(grade=grade)
      print(classes)
      students = Student.objects.filter(class_id__in=classes)
      print(students)
      results = Attendance.objects.filter(student__in=students)
      grade = ''
    else:
      results = Attendance.objects.all()
      print('1')

    context = {'results':results}
    return render(request,'runningattendance/result.html', context)




# def student_list(request):
#     search = request.GET.get('search')
#     if search:
#         student_list = Student.objects.filter(
#             Q(student_name=search)|
#             Q(student_id=search)|
#             Q(student_tel=search)|
#             Q(student_qq=search)|
#             Q(student_address__contains=search)
#         )
#     else:
#         search = ''
#         student_list = Student.objects.all()
#     context = {'students':student_list}
#     return render(request, 'infosys/inquir/list/student.html', context)