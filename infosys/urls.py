from django.urls import path
from . import views

app_name = 'infosys'

urlpatterns = [
    path("", views.student_list, name='index'),
    path("help", views.help, name='help'),
    path("student-list/", views.student_list, name='student_list'),
    path("student-add/", views.student_add, name='student_add'),
    path("student-delete/<str:id>/", views.delete_student, name='student_delete'),
    path("student-upload/", views.student_upload, name='student_upload'),
    path("student-detail/<str:pk>/", views.StudentDetailView.as_view(), name='student_detail'),
    path("class-list/", views.ClassListView.as_view(), name='class_list'),
    # path("class-detail/<int:pk>/", views.ClassDetailView.as_view(), name='class_detail'),
    path("class-detail/<int:pk>/", views.class_detail, name='class_detail'),
    path("class-upload/", views.class_upload, name='class_upload'),
    path("dormitory-list/", views.DormitoryListView.as_view(), name='dormitory_list'),
    # path("dormitory-list/", views.dormitory_list, name='dormitory_list'),
    # path("dormitory-detail/<str:pk>/", views.DormitoryDetailView.as_view(), name='dormitory_detail'),
    path("dormitory-detail/<str:pk>/", views.dormitory_detail, name='dormitory_detail'),
]
