from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:boardCode>', views.detail, name='detailBoard'),
    path('<str:boardCode>/<int:threadId>', views.detailThread, name='detailThread'),
]
