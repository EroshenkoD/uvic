from django.db import models
from django.db.models import Q
from relativefilepathfield.fields import RelativeFilePathField


class Project(models.Model):

    LIST_TECHNOLOGY = [("ICE", "ICE"), ("DCE", "DCE"), ("TEST", "TEST")]

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50, choices=LIST_TECHNOLOGY)
    image = RelativeFilePathField(path="projects/static/")

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(technology="ICE") | Q(technology="DCE"),
                                   violation_error_message="You can choose only ICE or DCE",
                                   name='check_technology')]

    def __str__(self):
        return self.title
