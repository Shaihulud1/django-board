from django.contrib import admin
from .models import Board, Thread

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'boardName', 'activity')

    def activity(self, obj):
        return 'YES' if obj.isActive > 0 else 'NO'


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'threadTitle', 'getboard', 'activity')

    def activity(self, obj):
        return 'YES' if obj.isActive > 0 else 'NO'
    def getboard(self, obj):
        return obj.boardFK.boardName


# Register your models here.
admin.site.register(Board, BoardAdmin)
admin.site.register(Thread, ThreadAdmin)
