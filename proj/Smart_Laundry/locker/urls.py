from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmartLockerList.as_view()),
    path('<int:pk>/', views.SmartLockerDetail.as_view()),
    path('using/<int:pk>/', views.SmartLockerUsing.as_view()),
    path('door/<int:pk>/', views.SmartLockerDoor.as_view()),
    path('error/<int:pk>/', views.SmartLockerError.as_view()),
    path('user/<int:pk>/', views.SmartLockerUser.as_view()),
    path('timer/<int:pk>/', views.SmartLockerTimer.as_view()),
    path('test/<int:pk>/', views.get_data),
    path('test/', views.get_data_test),
]