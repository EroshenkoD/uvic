import logging
from django.views import generic

from .models import Project


logger = logging.getLogger('main')


class IndexView(generic.ListView):
    logger.info('Test IndexView')
    template_name = 'projects/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        logger.warning('Test get_queryset')
        return Project.objects.all()


class DetailView(generic.DetailView):
    logger.info('Test DetailView')
    model = Project
    context_object_name = 'project'
    template_name = 'projects/detail.html'



