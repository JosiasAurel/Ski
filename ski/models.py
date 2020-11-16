from django.db import models

# Create your models here.


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Snippet {self.title} at {self.created_on}>"
