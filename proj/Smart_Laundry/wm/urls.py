from django.urls import path
from . import views

urlpatterns = [
    path('', views.WashingMachineList.as_view()),
    path('<int:pk>/', views.WashingMachineDetail.as_view()),
    path('using/<int:pk>/', views.WashingMachineUsing.as_view()),
    path('door/<int:pk>/', views.WashingMachineDoor.as_view()),
    path('error/<int:pk>/', views.WashingMachineError.as_view()),
    path('user/<int:pk>/', views.WashingMachineUser.as_view()),
    path('timer/<int:pk>/', views.WashingMachineTimer.as_view()),
    path('timer/<int:pk>/', views.WashingMachineTimer.as_view()),
    path('test/<int:pk>/', views.get_data),
    # path('test/', views.get_data),
    path('test/', views.get_data_test),
    # path('test/<int:pk>/', views.get_detail),
    # path('test/<int:pk>/', views.WashingMachineTest.as_view()),     
    # path('test/')
]