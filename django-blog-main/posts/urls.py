from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('post/<str:pk>', views.post, name='post'),
    path('post/<str:pk>', views.post, name='post'),
    path('delete/<int:id>/', views.delete_view),
    path('update/<int:id>/', views.update_view),
]