from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccessSystemList.as_view()),
    path('<int:pk>/', views.AccessSystemDetail.as_view()),
    path('door/<int:pk>/', views.AccessSystemDoor.as_view()),
    path('error/<int:pk>/', views.AccessSystemError.as_view()),
    path('user/<int:pk>/', views.AccessSystemUser.as_view()),
    path('test/<int:pk>/', views.get_data),
    path('test/', views.get_data_test),
]