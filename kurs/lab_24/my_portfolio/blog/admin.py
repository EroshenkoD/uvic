from django.contrib import admin

from .models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "get_categories", "last_modified", "body")
    list_filter = ("categories",)

    @staticmethod
    def get_categories(obj):
        return "\n".join([cat.name for cat in obj.categories.all()])


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "created_on", "post", "body")
    list_filter = ("author", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
