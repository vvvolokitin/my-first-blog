from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.post_list, name='post_list'),
]
