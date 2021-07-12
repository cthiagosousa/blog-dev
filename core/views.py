from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from .models import Post

# Post Methods
def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()

    return render(request, 'posts.html', {
        'posts': posts
    })

def create(request: HttpRequest) -> HttpResponse:
    return render(request, 'create_post.html')

def create_submit(request: HttpRequest) -> HttpResponseRedirect:
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.user
        
        if len(title.strip()) > 0 and len(description.strip()) > 0:
            Post.objects.create(title=title, description=description, author=author)        

    return redirect('/')
