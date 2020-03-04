from django import forms
from .models import Attendance, Takeleave

class AttendanceForm(forms.ModelForm):
    model = Attendance
    fields = ('student', 'inspector')