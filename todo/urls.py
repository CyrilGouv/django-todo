from todo.views import todo_list
from django.urls import path
from django.urls import path
from .views import todo_list

app_name = 'todos'

urlpatterns = [
    path('', todo_list)
]