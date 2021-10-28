import datetime

from django.db import models

# Create your models here.

class Message(models.Model):
    sname = models.CharField(max_length=30, unique=True)  # 字符串
    message = models.CharField(max_length=15)
    dat = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    class Meta:
        db_table = 'user_message'
