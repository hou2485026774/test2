from django.db import models

# Create your models here.
#数据库模型
'''
根据模型生成迁移文件，将迁移文件映射到数据库 生成表
python manage.py makemigrations stu 生成迁移文件
 python manage.py migrate 映射到数据库

'''
class Student(models.Model):
    sname = models.CharField(max_length=30,unique=True) #字符串
    spwd = models.CharField(max_length=15)

    #设置生成的表的信息
    class Meta:
        db_table = 't_stu2'
class Teacher(models.Model):
    tno = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=30)

    def __unicode__(self):
        return u'Teacher:%s'%self.tname

class Tcard(models.Model):
    teacher = models.OneToOneField(Teacher,primary_key=True,on_delete=models.CASCADE)
    major = models.CharField(max_length=30,unique=True)#一个老师只能教一科

    def __unicode__(self):
        return u'Tcard:%s'%self.major