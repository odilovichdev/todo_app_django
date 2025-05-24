from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


    @property
    def completed(self):
        return all(subtask.completed for subtask in self.subtasks.all())


class SubTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='subtasks')

    def __str__(self):
        return f"{self.title}"
