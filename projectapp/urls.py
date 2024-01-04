from django.urls import path
from . import views

# urlpatterns is a list of route configurations.
# Each configuration is created by calling the path function with a route and a view function.
# The name parameter is used to uniquely identify the route.
urlpatterns = [
    # The home route. When the user navigates to the root URL of the site (e.g., 'http://localhost:8000/'), 
    # the home view will be invoked.
    path('', views.home, name='home'),  
    
    # The blog index route. When the user navigates to 'http://localhost:8000/blog/', 
    # the blog_index view will be invoked.
    path('blog/', views.blog_index, name='blog_index'),
    
    # The blog detail route. This route includes a variable part (pk) in the URL. 
    # When the user navigates to a URL like 'http://localhost:8000/blog/1/', 
    # the blog_detail view will be invoked with pk set to 1.
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    # The login route. When the user navigates to 'http://localhost:8000/login/', 
    # the login_view will be invoked.
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]