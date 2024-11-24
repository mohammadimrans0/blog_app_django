from django.shortcuts import render, redirect
from .forms import PostForm
from posts.models import Post

def add_and_show_posts(request):
    # Handle form submission
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_and_show_posts')
    else:
        post_form = PostForm()

    # Fetch all posts to display
    data = Post.objects.all()

    # Render the template with the form and posts
    return render(request, 'add_and_show_posts.html', {'form': post_form, 'data': data})

# edit post
def edit_post(request, id):
    post = Post.objects.get(pk=id) 
    post_form = PostForm(instance=post)

    if request.method == 'POST': 
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid(): 
            post_form.save() 
            return redirect('add_and_show_posts') 
    
    return render(request, 'add_and_show_posts.html', {'form' : post_form})


# delete post
def delete_post(request, id):
    post = Post.objects.get(pk=id) 
    post.delete()
    return redirect('add_and_show_posts')
