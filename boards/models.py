from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.files.storage import FileSystemStorage

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
    threadImg    = models.FileField(
                        default='img/default.png',
                        upload_to='img/uploads/%Y/%m',
                        storage=FileSystemStorage(location='boards/static/boards',base_url='/uploads'),
                        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])]
                   )
    isActive     = models.IntegerField(default=1)

    def __str__(self):
        return self.threadTitle

class ThreadMessage(models.Model):
    threadFK      = models.ForeignKey(Thread, on_delete = models.CASCADE)
    textMessage   = models.TextField()
    authorIP      = models.CharField(max_length = 200)
    author        = models.CharField(default="anon", max_length = 50)
    pubDate       = models.DateTimeField(auto_now_add=True)
