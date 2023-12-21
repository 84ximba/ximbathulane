from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages



def blog_index(request):
    """
    This view returns all blog posts ordered by date in descending order.
    """
    # Get all blog posts and order them by date
    posts = BlogPost.objects.all().order_by('-date')
    
    # Render the blog_index.html template with the posts 
    return render(request, 'blog_index.html', {'posts': posts})  

def blog_detail(request, pk):
    """
    This view returns the details of a specific blog post.
    """
    try:
        # Get the blog post with the given primary key (pk)
        post = BlogPost.objects.get(pk=pk)  
    except BlogPost.DoesNotExist:
        # If the blog post does not exist, set post to None
        post = None
    # If post is None, return a response indicating that the blog post was not found
    if post is None:
        return HttpResponse("Blog post not found.")
    else:
        # If the blog post exists, render the blog_detail.html template with the post
        return render(request, 'blog_detail.html', {'post': post}) 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request):
    """
    This view returns the home page with all blog posts ordered by date in descending order.
    It requires the user to be logged in.
    """
    # Get all blog posts and order them by date
    posts = BlogPost.objects.all().order_by('-date')  
    
    # Render the home.html template with the user and posts
    return render(request, 'home.html', {'user': request.user, 'posts': posts}) 

def login_view(request):
    """
    This view handles user login.
    """
    if request.method == 'POST':
        # If the request method is POST, attempt to authenticate the user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If the user is authenticated, log them in and return a success message
            login(request, user)
            return HttpResponse("Logged in successfully.")
        else:
            # If the user is not authenticated, return an error message
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        # If the request method is not POST, render the login form
        return render(request, 'login.html')
def logout_view(request):
    """
    This view handles user logout.
    """
    logout(request)  # This line logs out the user.
    return redirect('home')  # This line redirects the user to the home page.