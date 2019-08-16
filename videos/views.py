from django.urls import reverse_lazy
from django.views import generic
from .forms import VideoCreateForm
from .models import Video
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from .forms import LoginForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'videos/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'videos/login.html'

class IndexView(generic.ListView):
    model = Video

class CreateView(generic.CreateView):
    model = Video
    form_class = VideoCreateForm
    success_url = reverse_lazy('videos:index')

class PlayView(generic.DetailView):
    model = Video
