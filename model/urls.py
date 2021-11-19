from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListStaff.as_view()),    
    path ('<int:pk>/', views.DetailStaff.as_view()),
    #path('managerlogin/', views.LoginView.as_view()),
]