from django.db import models
from  django.utils import  timezone
# Create your models here.

class List(models.Model):
    pass
    
class Item(models.Model):
    text = models.TextField(blank=False)
    logtime = models.DateTimeField('create_time',default=timezone.now)
    list = models.ForeignKey(List,related_name='item_list',default=None)

