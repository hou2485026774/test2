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