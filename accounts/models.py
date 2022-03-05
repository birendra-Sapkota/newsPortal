from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    phone_number = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=600)
    title_caption = models.CharField(max_length=500)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.CharField(max_length=600, null=True, blank=True)
    views_count = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
