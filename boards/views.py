from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect

from .forms import ThreadForm, ThreadMessageForm
from .models import Board, Thread, ThreadMessage

# Create your views here.
def index(request):
    boardsList = Board.objects.filter(isActive__gt = 0)
    context = {'boardsList': boardsList}
    return render(request, 'boards/index.html', context)

def detail(request, boardCode):
    boardDetail = get_object_or_404(Board, boardCode = boardCode, isActive__gt = 0)
    threadList = Thread.objects.filter(boardFK = boardDetail.id, isActive__gt = 0)
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            formObj = form.save(commit=False)
            formObj.boardFK = boardDetail
            formObj.save()
            return redirect('detailThread', boardCode = boardDetail.boardCode, threadId = formObj.id)
    else:
        form = ThreadForm()
    context = {'boardDetail': boardDetail, 'threadList': threadList, 'form': form}
    return render(request, 'boards/boardDetail.html', context)

def detailThread(request, boardCode, threadId):
    boardDetail = get_object_or_404(Board, boardCode = boardCode, isActive__gt = 0)
    threadDetail = get_object_or_404(Thread, boardFK = boardDetail.id, id = threadId, isActive__gt = 0)
    if request.method == "POST":
        form = ThreadMessageForm(request.POST)
        if form.is_valid():
            formObj = form.save(commit=False)
            formObj.authorIP = request.META['REMOTE_ADDR']
            formObj.threadFK = threadDetail
            formObj.save()
            #return http.HttpResponseRedirect('')
            form = ThreadMessageForm()
    else:
        form = ThreadMessageForm()
    messageList = ThreadMessage.objects.filter(threadFK = threadDetail.id)
    context = {'threadDetail': threadDetail, 'messageList': messageList, 'form': form}
    return render(request, 'boards/threadDetail.html', context)


    # class ThreadMessage(models.Model):
    #     threadFK      = models.ForeignKey(Thread, on_delete = models.CASCADE)
    #     textMessage   = models.TextField()
    #     authorIP      = models.CharField(max_length = 200)
    #     author        = models.CharField(default="anon", max_length = 50)
    #     pubDate       = models.DateTimeField(auto_now_add=True)
