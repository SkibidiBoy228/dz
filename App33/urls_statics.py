from django.urls import path
from . import views

urlpatterns = [
    path('', views.statics_page, name='statics'),
]
