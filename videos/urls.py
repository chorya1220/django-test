from django.urls import path
from .import views

app_name = 'videos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('upload/', views.CreateView.as_view(), name='upload'),
    path('play/<int:pk>/', views.PlayView.as_view(), name='play'),
]
