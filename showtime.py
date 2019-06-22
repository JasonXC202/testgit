import datetime
#from django.utils.timezone import utc
from django.utils import timezone
time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M;%S')
#time2= datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%Y-%m-%d %H:%M;%S')
time3 = timezone.now()
USE_TZ = True
print("本地时间:"+time1)
#print("UTC时间："+time2)
print(time3)


