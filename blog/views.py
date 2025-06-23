from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from .models import BlogPost, Comment, Category
from .forms import BlogPostForm, CommentForm

def blog_list(request):
    query = request.GET.get('q')
    if query:
        posts = BlogPost.objects.filter(title__icontains=query).order_by('-created_at')
    else:
        posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'posts': posts, 'query': query})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = comment_form.cleaned_data['author']
            comment.post = post
            comment.save()
            return redirect('blog_detail', slug=slug)
    else:
        comment_form = CommentForm()
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('blog_detail', slug=post.slug)
    else:
        form = BlogPostForm()
    return render(request, 'blog_create.html', {'form': form})
