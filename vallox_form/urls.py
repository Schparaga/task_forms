from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('vallox_form/', views.task_form, name='vallox_form'),
    path('task/', views.task, name='task'),
    path('task/<int:pk>', views.TaskFormView.as_view(), name='task-detail'),
    path('task/<int:pk>/update', views.TaskFormUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', views.TaskFormDeleteView.as_view(), name='task-delete'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
]
