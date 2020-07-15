from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def show_todos(request):
    """
    1. Берем данные из запроса и создаем объект TodoEditForm
       c этими данными
    2. Если объект todoEditForm is_valid, 
          берем очищенные данные cleaned_data и сохраняем в БД
       Иначе
          вернем объект todoEditForm и отобразим ошибки из него
    """
    app_name = 'Список дел'
    error_text = ''
    
    todos = Todo.objects.all()  # [ Todo1, Todo2, ... ]
    form = TodoForm()

    if request.GET and request.GET.get('todo_id'):
        todo_id = request.GET.get('todo_id')
        todo = Todo.objects.get(id=todo_id)
        form = TodoForm({
            'id': todo.id,
            'text': todo.text,
            'priority': todo.priority,
            'todo': todo.done
        })

    if request.POST:
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_todos_url')

    context = {
        'name': app_name,
        'todos': todos,
        'form': form,
        'error_text': error_text
    }
    return render(request, 'todo/show_todos.html', context)

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('show_todos_url')
