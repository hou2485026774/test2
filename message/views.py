from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def show_message(request):
    username = request.GET.get('username')
    mes = Message.objects.all()
    return render(request,'show_message.html',{'mes':mes,'username':username})


def make_message(request):
    message = request.GET.get('mess')
    username = request.session['username']
    mes = Message(sname=username,message=message)
    mes.save()
    return redirect('/message',{'username':username})

def delete_message(request):

    username = request.GET.get('username')


    #删除留言
    Message.objects.get(sname=username).delete()

    return redirect('/message')