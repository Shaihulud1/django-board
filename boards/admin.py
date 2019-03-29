from django.contrib import admin
from django.conf import settings
from .models import Board, Thread, ThreadMessage

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'boardName', 'activity')

    def activity(self, obj):
        return 'YES' if obj.isActive > 0 else 'NO'

    activity.admin_order_field = 'isActive'


# class ThreadMessagAdmin(admin.ModelAdmin):
#     list_display = ('id', 'author', 'authorIP', 'threadTitle', 'pubDate', 'textMessageShort')
#
#     def threadTitle(self, obj):
#         return obj.threadFK.threadTitle
#
#     def textMessageShort(self, obj):
#         stringLen = 20
#         return "%s..." % obj.textMessage[0:stringLen] if len(obj.textMessage) > stringLen else obj.textMessage
#
#     threadTitle.admin_order_field = 'threadTitle'
#     textMessageShort.admin_order_field = 'textMessage'

class ThreadMessageInline(admin.StackedInline):
    model = ThreadMessage

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'threadTitle', 'getboard', 'activity')
    inlines = [ThreadMessageInline]
    def activity(self, obj):
        return 'YES' if obj.isActive > 0 else 'NO'

    def getboard(self, obj):
        return obj.boardFK.boardName

    getboard.admin_order_field = 'boardFK'
    activity.admin_order_field = 'isActive'


# Register your models here.
admin.site.register(Board, BoardAdmin)
admin.site.register(Thread, ThreadAdmin)
#admin.site.register(ThreadMessage, ThreadMessagAdmin)
