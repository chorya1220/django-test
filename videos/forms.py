from django import forms
from .models import Video
from django.contrib.auth.forms import (
    AuthenticationForm
)

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class VideoCreateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = {'title', 'description', 'thumbnail', 'upload'}

        widgets = {
            'title': forms.TextInput(attrs={
                 'class': 'form-control',
            }),
            'decription': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
            'upload': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
        }
