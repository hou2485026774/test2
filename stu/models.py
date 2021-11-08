from django.db import models

# Create your models here.
#数据库模型
'''
根据模型生成迁移文件，将迁移文件映射到数据库 生成表
python manage.py makemigrations stu 生成迁移文件
 python manage.py migrate 映射到数据库

'''
#用户表
class User(models.Model):
    sname = models.CharField(max_length=30,unique=True) #字符串
    spwd = models.CharField(max_length=15)

    #设置生成的表的信息
    class Meta:
        db_table = 't_stu2'
#老师信息表
class Teacher(models.Model):
    tno = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=30)
    t_img = models.ImageField(upload_to='img',null=True)

    def __unicode__(self):
        return u'Teacher:%s'%self.tname
#教师科目表
class Tcard(models.Model):
    teacher = models.OneToOneField(Teacher,primary_key=True,on_delete=models.CASCADE)
    major = models.CharField(max_length=30,unique=True)#一个老师只能教一科

    def __unicode__(self):
        return u'Tcard:%s'%self.major

#一对多的关系模型
#班级表
class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)


#学生表
class Xuesheng(models.Model):
    xno = models.AutoField(primary_key=True)
    xname = models.CharField(max_length=30)
    cno = models.ForeignKey(Clazz,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.xname

