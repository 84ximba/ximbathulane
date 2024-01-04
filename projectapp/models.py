from django.db import models

class BlogPost(models.Model):
    # The title of the blog post. It's a character field with a maximum length of 200 characters.
    title = models.CharField(max_length=200)
    
    # The body of the blog post. 
    #It's a text field, which is a large multi-line input field that allows the user to enter multiple lines of text.
    body = models.TextField()

    # The signature of the author of the blog post. 
    # It's a character field with a maximum length of 140 characters. 
    # If no signature is provided, it will default to "Your Default Signature".
    signature = models.CharField(max_length=140, default="Thulane Ximba | ximba.thulane01@gmail.com") 

     # The date and time the blog post was created. 
     # It's a date-time field that automatically sets itself to the current date and time when the blog post is first created.
    date = models.DateTimeField(auto_now_add=True) 
