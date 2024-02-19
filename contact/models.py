from django.db import models


class ContactRequest(models.Model):
    """ Model for Contact for """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=50)
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        read_icon = "✅" if self.read else "✉"
        return f'Message from {self.name} | {self.title} | {read_icon}'
