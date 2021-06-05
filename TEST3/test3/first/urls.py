from . import views
from django.urls import path


urlpatterns = [
    # path('sensor/', views.SensorViewSet.as_view())
    # path('post/', views.post_list),
    #path('post/get_data/', views.SensorViewSet.as_view())
    # path('api1/', views.get_data),
    path('', views.get_data),
    path('<int:pk>/', views.get_detail),    
    # path('<int:pk>/', views.SensorDetail.as_view()),    
]