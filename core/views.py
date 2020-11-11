from django.shortcuts import render
from django.views.generic import ListView , DetailView , UpdateView
from .models import *
from django.urls import reverse_lazy



# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'core/core_list.html'


class SinglelView(DetailView):
    model = Core
    template_name = "core/single.html"
    context_object_name = 'post'
    
