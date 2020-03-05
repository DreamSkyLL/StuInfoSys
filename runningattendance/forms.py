from django import forms
from .models import Attendance, Takeleave

class CheckinForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('student', 'inspector')
