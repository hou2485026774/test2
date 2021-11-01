import datetime

from django.db import models

# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)  # 字符串
    message = models.CharField(max_length=15)
    class Meta:
        db_table = 'user_message'
