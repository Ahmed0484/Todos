from django.urls import  path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('all/',TodoListView.as_view(),name='all'),
    path('add/',TodoCreateView.as_view(),name='add'),
    path('todo/<int:pk>/',TodoDetailView.as_view(),name='detail'),
    path('edit/<int:pk>/',TodoUpdateView.as_view(),name='edit'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='delete')

]