from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Todo


# Create your views here.

def index(request):
    return render(request,'index.html')

class TodoListView(ListView):
    paginate_by = 3
    model = Todo
    template_name = 'all.html'
    def get_queryset(self):
        return Todo.objects.all().order_by('-id')

class TodoCreateView(CreateView):
    model = Todo
    fields = ['text']
    template_name = 'add.html'
    success_url = '/all/'


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['text']
    template_name = 'edit.html'
    success_url = '/all/'


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = '/all/'
