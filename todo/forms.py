from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['id', 'text', 'priority', 'done']

class TodoEditForm(forms.Form):
    id = forms.IntegerField(
        required=False
    )
    text = forms.CharField(
        max_length=255,
        required=True
    )
    priority = forms.IntegerField(
        required=True
    )
    done = forms.BooleanField(
        required=False
    )