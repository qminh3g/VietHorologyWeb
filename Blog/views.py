from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogModel
# Create your views here.
class HomeView(ListView):
    model = BlogModel
    template_name = 'home.html'
class ArticleDetailView(DetailView):
    model = BlogModel
    context_object_name = 'blog' 
    template_name = 'article_detail.html'
def login(request):
    return render(request,'login.html')
    
