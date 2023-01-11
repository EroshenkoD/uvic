from django.shortcuts import render
from django.views import generic

from .forms import CommentForm
from .models import Post, Comment


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.category_objects.get_post_with_rating_of_discussion()


def category(request, category):
    posts = Post.category_objects.get_post_by_category_with_rating_of_discussion(category)
    context = {"category": category, "posts": posts}
    return render(request, "blog/category.html", context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "blog/detail.html", context)
