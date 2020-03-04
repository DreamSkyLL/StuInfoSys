from django import forms
from .models import Student, Event

class StudentForm(forms.ModelForm):
    dormitory_id = forms.CharField(max_length=20, required=False)
    bed_num = forms.CharField(max_length=2, required=False)

    class Meta:
        model = Student
        fields = ('student_id', 'student_name', 'student_sex', 'student_birth', 'student_address', 'student_tel', 'student_qq', 'class_id')

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('content',)