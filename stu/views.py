import math
import os

import django.db.models.query
from django.http import HttpResponse
from django.shortcuts import render, redirect
from stu.models import *
# Create your views here.
def index(request):

    return render(request,'login.html')

#登录功能
def login(request):
    #接受参数
    username = request.POST.get('name')
    password = request.POST.get('password')
    print(username,'+',password)
    response = HttpResponse()
    # request.session['username']=username
    response.set_cookie('user',username)
    #登录逻辑处理
    if username and password:
        #判断查询
        c = User.objects.filter(sname=username,spwd=password).count()
        if c==1:
            return render(request,'home.html')
    return HttpResponse('登录失败')
# def home(request):
#     username = request.session['username']
#     return render(request,'home.html',username)
import pymysql
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
        stu = User(sname=username,spwd=password)
        #插入数据库
        stu.save()
        return HttpResponse('注册666')
    return HttpResponse('注册777')
#处理分页
def page(num,size=2):
    #接受页码
    num = int(num)
    #计算总记录数
    total = User.objects.count()
    #总页数
    total_page =math.ceil(total*1.0/size)
    #判断是否越界
    if num<1:
        num = 1
    elif num>total_page:
        num=total_page
    user = User.objects.all()[((num-1)*size):num*size]
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
    size = request.GET.get('size',5)
    # print(size)
    #查询数据
    user = User.objects.all()
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
    stu = User.objects.get(sname=username)
    stu.delete()
    return redirect('/user/show_user2')
#原生sql查询时，将结果转化为字典 直接传参
def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]
from django.db import connection
#表连接查询
def JoinShow(request):
    # teacher = Teacher.objects.all()#查询老师表信息
    # tcard1 = Teacher.objects.all()[0].tcard#根据老师表信息查询教学科目表中该老师教授的科目
    # # print(type(teacher))
    # # print(django.db.models.query.QuerySet(tcard1))
    # return render(request,'show_teacher.html',{'tcard1':django.db.models.query.QuerySet(tcard1),'teacher':teacher})
    cursor  = connection.cursor()
    cursor.execute("select * from stu_teacher a,stu_tcard b where a.tno=b.teacher_id")
    values = dictfetchall(cursor)
    print(values)
    cursor.close()
    connection.close()
    return render(request,'show.html',{'values':values})
def XueSheng(request):
    # c = Xuesheng.objects.first().clazz
    x = Clazz.objects.first()
    # print(c)
    print(x)
    return HttpResponse('END')

#原生图片上传
def techer_register(request):
    if request.method =='GET':
        return render(request,'t_r.html')
    elif request.method=='POST':
        t_name = request.POST.get('t_name','')
        t_img = request.FILES.get('t_img','')
        # print(t_img)
        import os
        #判断目录是否存在
        if not os.path.exists('media'):
            os.makedirs('media')
        with open(os.path.join(os.getcwd(),'media',t_img.name),'wb') as fw:
            #一次性读取 写入
            fw.write(t_img.read())

            #分块写入 提高效率
            for ck in t_img.chunks():
                fw.write(ck)
        return HttpResponse('成功！')
    else:
        return render(request,'t_r.html')
#django 上传
def techer_register2(request):
    if request.method =='GET':
        return render(request,'t_r.html')
    elif request.method=='POST':
        t_name = request.POST.get('t_name','')
        t_img = request.FILES.get('t_img','')
        major = request.POST.get('major','')
        #插入数据库
        Teacher.objects.create(tname=t_name,t_img=t_img)
    return HttpResponse('上传成功')

#图片下载---未完成
def download(request):
    img = request.GET.get('img','')
    #获取图片文件名
    filename = img[img.rindex('/')+1]
    return None