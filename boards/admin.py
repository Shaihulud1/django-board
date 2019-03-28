from django.contrib import admin
from .models import Board, Thread

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'boardName', 'isActive')
    list_filter = ['isActive']

# Register your models here.
admin.site.register(Board, BoardAdmin)
admin.site.register(Thread)
