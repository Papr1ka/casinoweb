from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
    name = 'Casino'
    
    posts = Post.objects.all()
    
    
    return render(request, 'dashboard/main.html', context={'app_name': name, 'posts': posts})

def post(request):
    pass