from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=50)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def _str__(self):
        return f'Message from {self.name}'
