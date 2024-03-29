from django.shortcuts import render,redirect,Http404
from django.http import HttpResponse
from lists.models import Item,List
from lists.forms import ItemForm,EMPTY_ITEM_ERROR,ExistingListItemForms,DUPLICATE_ITEM_ERROR
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.
def get_html(self):
	aa = Item.objects.all() 
	return render(self,'home1.html',{'showitems': aa})
	
def home_page(self):
	#try:
	#return HttpResponse('<html><title>To-Do lists</title></html>')
		#if self.method == 'POST':
			#new_text = self.POST['text']
			#Item.objects.create(text=new_text)
		   # return redirect('/lists/the-only-list-in-the-world/')
	#else:
		#new_text = ""
		#aa = Item.objects.all()
		#messages.success(self,'添加成功')
	return render(self,'home.html',{'form':ItemForm()})

#旧的view_list方法
'''	 
def view_list(self,list1_id):
	list_ = List.objects.get(id=list1_id)
	err1= None
	form =ItemForm()
	if self.method == 'POST':
		try:
			item = Item.objects.create(text=self.POST['text'],list = list_)
			item.full_clean()
			item.save()
			#return redirect(f'/lists/{list_.id}/')
			return redirect(list_)
		except ValidationError:
			#list_.delete()
			err1 = "You can't have an empty list item" 
	#except List.DoesNotExist:
		#raise Http404("HTTP Status 404 - Not Found")  
	#aa1=Item.objects.filter(list=list_)
	#aa1 = Item.objects.all()
	#return render(self,'list.html',{'test':aa1})
	return render(self,'list.html',{'list':list_,'form':form,'error':err1})
'''

#form类的view_list方法
def view_list(self, list1_id):
	list1 = List.objects.get(id=list1_id)
	form_list = ExistingListItemForms(for_list=list1)
	if self.method == 'POST':
		form_list = ExistingListItemForms(for_list=list1,data=self.POST)	  
		if form_list.is_valid():
			#Item.objects.create(text=self.POST['text'], list=list_)
			form_list.save(for_list=list1)
			return redirect(list1)
	return render(self, 'list.html', {'list': list1, 'form': form_list})


#旧的new_list方法
'''
def new_list(self):
	#aa1 = Item.objects.all()
	list1 = List.objects.create()
	item = Item.objects.create(text=self.POST['text'],list = list1)
	try:
	#return redirect('/lists/the-only-list-in-the-world)
		item.full_clean()
		item.save()
	except ValidationError:
		list1.delete()
		err1 = "You can't have an empty list item"
		return render(self,'home.html',{'error':err1})
	#return redirect(f'/lists/{list1.id}/')
	#return redirect('view_list1',list1.id)
	return redirect(list1)
	#return render(self,'list.html',{'items':aa1})
'''	 
  
#form类的new_list方法
def new_list(self):
	form_list = ItemForm(data=self.POST)
	if form_list.is_valid():
		list1 = List.objects.create()
		'''
		instance = form.save(commit=False)
		instance.created_by = self.list
		#Item.objects.create(text=self.POST['text'],list=list1)
		instance.save()
		'''
		form_list.save(for_list=list1)
		return redirect(list1)
	else:
		return render(self,'home.html',{"form":form_list})
 
def add_item(self,list1_id):
	list_ = List.objects.get(id=list1_id) 
	Item.objects.create(text=self.POST['text'],list=list_)
	#return render(self,'list.html',{'list':list_})
	return redirect(f'/lists/{list_.id}/')
	
def other_list(self,list1_id):
	list_ = List.objects.get(id=list1_id) 
	Item.objects.create(text=self.POST['text'],list=list_)
	#aa1 = Item.objects.filter(list=list_)
	#list_ = List.objects.create()
	return render(self,'list.html',{'list':list_})
	#return render(self,'list.html',{'test':aa1})
	