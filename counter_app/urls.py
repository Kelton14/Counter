from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    path('by_two', views.by_two),
    path('by_x', views.by_x),
]