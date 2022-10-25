from . import views
from django.urls import path

urlpatterns = [

    path('',views.task,name='task'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvindex/',views.ToDoListView.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.ToDoDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.ToDoUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.ToDoDeleteView.as_view(),name='cbvdelete')


]
