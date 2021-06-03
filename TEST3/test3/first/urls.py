from . import views
from django.urls import path


urlpatterns = [
    # path('sensor/', views.SensorViewSet.as_view())
    path('post/', views.post_list)
]