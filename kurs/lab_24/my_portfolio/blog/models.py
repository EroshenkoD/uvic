from django.db import models
from django.db.models import Count, Max
from django.db.models.functions import Round


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.author


class PostManager(models.Manager):

    def get_post_with_rating_of_discussion(self):
        max_count = super().get_queryset().annotate(
            n_com=Count('comment')).aggregate(max_count=Max('n_com'))['max_count']

        return super().get_queryset().prefetch_related('categories').annotate(
            rating=Round(((Count('comment')*1.0)/max_count), 2))

    def get_post_by_category_with_rating_of_discussion(self, category):
        max_count = super().get_queryset().annotate(
            n_com=Count('comment')).aggregate(max_count=Max('n_com'))['max_count']

        return super().get_queryset().prefetch_related('categories').annotate(
            rating=Round(((Count('comment')*1.0)/max_count), 2)).filter(
            categories__name__contains=category).order_by("-created_on")


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    objects = models.Manager()
    category_objects = PostManager()

    def __str__(self):
        return self.title