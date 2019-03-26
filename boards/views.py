from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Board, Thread

# Create your views here.
def index(request):
    boardsList = Board.objects.filter(isActive__gt = 0);
    context = {'boardsList': boardsList}
    return render(request, 'boards/index.html', context)

def detail(request, boardCode):
    boardDetail = get_object_or_404(Board, boardCode = boardCode, isActive__gt = 0)
    threadList = Thread.objects.filter(boardFK = boardDetail.id, isActive__gt = 0)
    context = {'boardDetail': boardDetail, 'threadList': threadList}
    return render(request, 'boards/boardDetail.html', context)

def detailThread(request, boardCode, threadId):
    boardDetail = get_object_or_404(Board, boardCode = boardCode, isActive__gt = 0)
    threadDetail = get_object_or_404(Thread, boardFK = boardDetail.id, id = threadId, isActive__gt = 0)
    context = {'threadDetail': threadDetail}
    return render(request, 'boards/threadDetail.html', context)
