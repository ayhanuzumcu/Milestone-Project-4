from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('delivery_info/', views.delivery_info, name='delivery_info'),
    path('contact_info/', views.contact_info, name='contact_info'),
]