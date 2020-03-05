from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.db.models import Q
from django.views.generic import ListView, CreateView
from .forms import CheckinForm
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
    return render(request,'runningattendance/result/list/running.html', context)


class CheckinView(CreateView):
  def get(self, request, *args, **kwargs):
    return render(request, 'runningattendance/check/running.html')

  def post(self, request, *args, **kwargs):
    form = CheckinForm(data=request.POST)
    if form.is_valid():
      form.save()
      print(form.student)
    else:
      return HttpResponseBadRequest('格式错误！')
    return redirect('runningattendance:checkin')
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