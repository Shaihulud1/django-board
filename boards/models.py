from django.db import models
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Board(models.Model):
    boardName = models.CharField(max_length = 50)
    boardCode = models.CharField(max_length = 3)
    boardDesc = models.TextField()
    boardImg  = models.ImageField(
                        default='img/default.png',
                        upload_to='img/uploads/%Y/%m',
                        storage=FileSystemStorage(location='boards/static/boards',base_url='/uploads')
                   )
    isActive  = models.IntegerField(default=1)

    def imagePreview(self):
        return mark_safe('<img src="/static/boards/%s" width="200" height="150" />' % (self.boardImg))
    imagePreview.short_description = 'Current image'
    imagePreview.allow_tags = True

    def __str__(self):
        return self.boardName


class Thread(models.Model):
    boardFK      = models.ForeignKey(Board, on_delete=models.CASCADE)
    threadTitle  = models.TextField()
    threadDesc   = models.TextField()
    threadAuthor = models.CharField(default="anon", max_length = 50)
    pubDate      = models.DateTimeField(auto_now_add=True)
    threadImg    = models.ImageField(
                        default='img/default.png',
                        upload_to='img/uploads/%Y/%m',
                        storage=FileSystemStorage(location='boards/static/boards',base_url='/uploads'),
                   )
    isActive     = models.IntegerField(default=1)

    def imagePreview(self):
        return mark_safe('<img src="/static/boards/%s" width="200" height="150" />' % (self.threadImg))
        imagePreview.short_description = 'Current image'
        imagePreview.allow_tags = True

    def __str__(self):
        return self.threadTitle


class ThreadMessage(models.Model):
    threadFK      = models.ForeignKey(Thread, on_delete = models.CASCADE)
    textMessage   = models.TextField()
    authorIP      = models.CharField(max_length = 200)
    author        = models.CharField(default="anon", max_length = 50)
    pubDate       = models.DateTimeField(auto_now_add=True)
