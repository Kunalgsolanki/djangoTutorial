import uuid
from django.db import models

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Todo(BaseModel):
    todo_title = models.CharField(max_length=100)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False)
