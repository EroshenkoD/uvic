from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):

    list_display = ("title", "technology", "description")
    list_filter = ("technology",)
    fieldsets = (
        ("Title", {
            "fields": (("title",),)
        }),
        ("TaI", {
            "fields": (("technology", "image"),)
        }),
        ("Description", {
            "fields": (("description",),)
        }),
    )


admin.site.register(Project, ProjectAdmin)

