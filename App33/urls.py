from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                   
    path('hello/', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('lottery/', views.lottery, name='lottery'),    
    path('statics/', views.statics_page, name='statics'),
    path('http-help/', views.http_help, name='http_help'),
    path('product/add/', views.product_add, name='product_add'),
    path('delivery/', views.delivery, name='delivery'),
]
