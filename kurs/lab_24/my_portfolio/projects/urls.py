from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'projects'
urlpatterns = [
    path("", cache_page(60*2)(views.IndexView.as_view()), name="index"),
    path("<int:pk>/", cache_page(60*2)(views.DetailView.as_view()), name="detail"),
]
