from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todo_list': todos
    }
    
    return render(request, 'todo_list2.html', context)
