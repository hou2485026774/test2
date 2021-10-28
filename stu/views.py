import math

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):

    return render(request,'login.html')

#登录功能
def login(request):
    #接受参数
    username = request.GET.get('name')
    password = request.GET.get('password')
    request.session['username']=username
    #登录逻辑处理
    if username and password:
        #判断查询
        c = Student.objects.filter(sname=username,spwd=password).count()
        if c==1:
            return render(request,'home.html',{'session':request.session['username']})
    return HttpResponse('登录失败')
# def home(request):
#     username = request.session['username']
#     return render(request,'home.html',username)
#跳转注册
def to_register(request):
    return render(request,'register.html')
#注册功能
def register(request):
    # 接受参数
    username = request.POST.get('name')
    password = request.POST.get('password')
    # 注册逻辑处理
    if username and password:
        #创建数据模型
        stu = Student(sname=username,spwd=password)
        #插入数据库
        stu.save()
        return HttpResponse('注册666')
    return HttpResponse('注册777')
#处理分页
def page(num,size=2):
    #接受页码
    num = int(num)

    #计算总记录数
    total = Student.objects.count()
    #总页数
    total_page =math.ceil(total*1.0/size)

    #判断是否越界
    if num<1:
        num = 1
    elif num>total_page:
        num=total_page

    user = Student.objects.all()[((num-1)*size):num*size]
    return user,num
def show_user(request):
    #接受参数
    num = request.GET.get('num',1)
    #处理分页请求
    user,n = page(num)

    #上一页 下一页
    pre_page = n-1
    next_page = n+1

    return render(request,'show_user.html',{'user':user,'pre_page':pre_page,'next_page':next_page})#将值传给前端页面

from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
#Django分页
def show_user2(request):
    #获取当前页面
    num = request.GET.get('num',1)
    size = request.GET.get('size',1)
    # print(size)
    #查询数据
    user = Student.objects.all()
    #创建分页对象
    pager = Paginator(user,int(size))
    #获取当前页的数据
    try:
        page_data = pager.page(int(num))
    except PageNotAnInteger:
        page_data = pager.page(1)#第一页
    except EmptyPage:
        page_data = pager.page(pager.num_pages)#最后一页
    return render(request,'show_user.html',{'pager':pager,"page_data":page_data})

#删除数据
def delete(request):
    username = request.GET.get('sname')
    stu = Student.objects.get(sname=username)

    stu.delete()
    return redirect('/user/show_user2')