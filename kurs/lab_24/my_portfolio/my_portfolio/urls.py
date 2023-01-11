from django.conf import settings
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    path("admin/", admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("order_project/", include("order_project.urls")),
]