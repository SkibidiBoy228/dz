from django.urls import path
from App33.views import login_view
from .views import profile_view
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
    path("user/", views.user_form),
    path("seed-page/", views.seed_page, name="seed_page"),
    path("seed/", views.seed, name="seed"),
    path("login/", login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]
