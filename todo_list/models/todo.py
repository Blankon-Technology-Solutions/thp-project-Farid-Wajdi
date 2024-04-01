import uuid
from django.db import models
from todo_list.models import User


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nCompleted: {self.completed}"
