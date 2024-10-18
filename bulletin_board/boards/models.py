from django.db import models

# Create your models here.
class Board(models.Model):
    # author
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

class Comment(models.Model):
    # author
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)