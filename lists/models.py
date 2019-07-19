from django.db import models
from  django.utils import  timezone
from django.core.urlresolvers import reverse
#from django.urls import resolvers

# Create your models here.

class List(models.Model):

	def get_absolute_url(self):
		return reverse('view_list1',args=[self.id])
	
class Item(models.Model):
	text = models.TextField(blank=False,default='')
	logtime = models.DateTimeField(name='create_time',default=timezone.now)
	list = models.ForeignKey(List,related_name='item_list',default=None)

	class Meta:
		unique_together = ('list','text')
	
	def __str__(self):
		return self.text
