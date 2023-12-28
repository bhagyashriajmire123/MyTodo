from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Task

class CustomerLoginview(LoginView):
    template_name= 'xyz/login.html'
    fields = '__all__'
    redirect_authenticated_user=True
    





class TaskList(ListView):
    model=Task
    context_object_name='tasks'
    
class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
    template_name= 'xyz/task_detail.html'
    
class TaskCreate(CreateView):
    model=Task
    fields = '__all__'
    success_url= reverse_lazy('tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url= reverse_lazy('tasks')
    
class TaskDelete(DeleteView):
    model= Task
    context_object_name='task'
    success_url= reverse_lazy('tasks')