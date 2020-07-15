from django.urls import path
from .views import show_todos, delete_todo

urlpatterns = [
    path('', show_todos, name='show_todos_url'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo_url'),
]