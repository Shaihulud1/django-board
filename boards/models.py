from django.db import models

# Create your models here.
class Board(models.Model):
    boardName = models.CharField(max_length = 50)
    boardCode = models.CharField(max_length = 3)
    boardDesc = models.TextField()
    isActive  = models.IntegerField(default=1)

class Thread(models.Model):
    boardFK      = models.ForeignKey(Board, on_delete=models.CASCADE)
    threadTitle  = models.TextField()
    threadDesc   = models.TextField()
    threadAuthor = models.CharField(max_length = 50)
    pubDate      = models.DateTimeField(auto_now_add=True)
    isActive     = models.IntegerField(default=1)
