from jazz_app import views
from django.urls import path

urlpatterns = [
    path('', views.start),
    path('events/', views.event),
    path('main/', views.start),
    path('lives/', views.online),
    path('in_live/', views.live),
]