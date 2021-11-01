# import datetime
# print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
from stu.models import *

cls1 = Clazz.objects.first()
print(cls1)