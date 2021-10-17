from django.shortcuts import render, redirect
from blog.models import Post, Comment
from .forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid(): #TODO unter zl 36 else einfueg.
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
            return redirect("blog_detail",pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)

def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk) # comments haben nur einen foreign key? dh ich kann nur alle comments zu einem post loeschen oder gar keins?
    post = comment.post
    if request.method == 'POST':
        comment.delete()
    return redirect("blog_detail",pk=post.pk)