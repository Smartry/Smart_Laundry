from . import views
from django.urls import path


urlpatterns = [
    path('sensor/', views.ServoList.as_view())
]