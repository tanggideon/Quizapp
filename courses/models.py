from django.db import models
from home.models import BaseModel, Course


class Resource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=256)
    resource = models.FileField(upload_to="files", null=True)
    description = models.TextField()

    def __str__(self):
        return self.title