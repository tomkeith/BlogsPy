from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title