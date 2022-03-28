from django.db import models

class Post(models.Model):
  # author
  # image 
  title = models.CharField(max_length=255)
  content = models.TextField()
  # category
  # tag
  counted_view = models.PositiveIntegerField(default=0)
  status = models.BooleanField(default=False)
  published_date = models.DateTimeField(null=True)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

