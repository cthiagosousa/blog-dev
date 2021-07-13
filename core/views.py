from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.http.request import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Post

# Post Methods
def get_all_post(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()

    return render(request, 'posts.html', {
        'user': request.user,
        'is_anonymous': request.user.is_anonymous,
        'posts': posts
    })

@login_required(login_url='/login')
def create_post(request: HttpRequest) -> HttpResponse:
    return render(request, 'create_post.html')

@login_required(login_url='/')
def create_post_submit(request: HttpRequest) -> HttpResponseRedirect:
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        author = request.user
        
        if len(title.strip()) > 0 and len(description.strip()) > 0:
            Post.objects.create(title=title, description=description, author=author)        

    return redirect('/')

@login_required(login_url='/')
def update_post(request: HttpRequest, post_id: int) -> HttpResponse:
    post: Post = Post.objects.get(id=post_id)
    
    return render(request, 'create_post.html', {
        'id': post_id,
        'title': post.title,
        'description': post.description,
    })

@login_required(login_url='/')
def update_post_submit(request: HttpRequest) -> HttpResponseRedirect:
    if request.POST:
        post_id = request.GET.get('id')
        post: Post = Post.objects.get(id=post_id)
        
        if post:
            title = request.POST.get('title')
            description = request.POST.get('description')
            created_at = post.created_at
            author = post.author
        
            if post.author == request.user:
                Post.objects.filter(id=post_id).update(
                    title=title,
                    description=description,
                    author=author,
                    created_at=created_at,
                )
    
    return redirect('/user/admin')

@login_required(login_url='/')
def delete_post(request: HttpRequest, post_id: int) -> HttpResponseRedirect:
    post: Post = Post.objects.get(id=post_id)
    
    if post.author == request.user:
        Post.objects.filter(id=post_id).delete()
    
    return redirect('/user/admin')


# User Methods
def login_user(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')

def login_user_submit(request: HttpRequest) -> HttpResponseRedirect:
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
    
    return redirect('/login')

def logout_user(request: HttpRequest) -> HttpResponseRedirect:
    logout(request)
    
    return redirect('/')

@login_required(login_url='/')
def user_administration(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(author=request.user)
    
    return render(request, 'user_administration.html', {
        'user': request.user,
        'posts': posts,
    })
