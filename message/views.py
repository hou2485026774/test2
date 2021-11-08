import json

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *


def show_message(request):
    #--翻页
    num = request.GET.get('num',1)
    size = request.GET.get('size',10)
    # print("-----",size)
    username = request.GET.get('username')
    print("sss",username)
    mes = Message.objects.all()

    pager = Paginator(mes,int(size))
    try:
        page_data = pager.page(int(num))
    except PageNotAnInteger:
        page_data = pager.page(1)  # 第一页
    except EmptyPage:
        page_data = pager.page(pager.num_pages)
    return render(request,'show_message.html',{'mes':mes,'username':username,'pager':pager,"page_data":page_data})


def make_message(request):

    message = request.GET.get('mess')
    username = request.session['username']
    if len(message)==0:
        return redirect('/message', {'username': username})
    mes = Message(sname=username,message=message)
    mes.save()
    return redirect('/message',{'username':username})

def delete_message(request):

    id = request.GET.get('id')
    #删除留言
    Message.objects.get(id=id).delete()

    return redirect('/message')


def update_message(request):

    #获取修改请求的数据
    id = request.GET.get('id')

    mes = Message.objects.filter(id=id)
    return render(request,'update_message.html',{'mes':mes})


def update(request):

    id = request.GET.get('id')
    mes = request.GET.get('mes')
    Message.objects.filter(id=id).update(message=mes)
    return redirect('/message')
#JSON数据
from django.core import serializers
def ShowJson(request):
    result = {"message": 'success', "code": '0', "data": []}
    mes = Message.objects.all()
    result["data"] = serializers.serialize('python',mes)
    return HttpResponse(json.dumps(result),content_type="application/json")

