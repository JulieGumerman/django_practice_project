from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        'author': 'Julie',
        'title': 'Haiii',
        'content': 'I love whoodles',
        'date': 'Thursday, Day, Year'
    },
    {
        'author': 'Seymour Bullfrogs',
        'title': 'Bullfrogs Forever',
        'content': 'Jeremiah was one...',
        'date': 'Friday, Day, Year'
    },    
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})