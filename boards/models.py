from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Board(models.Model):
    boardName = models.CharField(max_length = 50)
    boardCode = models.CharField(max_length = 3)
    boardDesc = models.TextField()
    boardImg  = models.FilePathField(default='img/default.png')
    isActive  = models.IntegerField(default=1)

    def __str__(self):
        return self.boardName

class Thread(models.Model):
    boardFK      = models.ForeignKey(Board, on_delete=models.CASCADE)
    threadTitle  = models.TextField()
    threadDesc   = models.TextField()
    threadAuthor = models.CharField(default="anon", max_length = 50)
    pubDate      = models.DateTimeField(auto_now_add=True)
    threadImg    = models.FileField(default='static/boards/img/default.png', upload_to='static/boards/img/uploads/%Y/%m', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    isActive     = models.IntegerField(default=1)

    def __str__(self):
        return self.threadTitle
