from django.shortcuts import render,redirect,Http404
from django.http import HttpResponse
from lists.models import Item,List
from django.contrib import messages

# Create your views here.
def get_html(self):
    aa = Item.objects.all() 
    return render(self,'home1.html',{'showitems': aa})
    
def home_page(self):
    #try:
    #return HttpResponse('<html><title>To-Do lists</title></html>')
        #if self.method == 'POST':
            #new_item_text = self.POST['item_text']
            #Item.objects.create(text=new_item_text)
           # return redirect('/lists/the-only-list-in-the-world/')
    #else:
        #new_item_text = ""
        #aa = Item.objects.all()
        #messages.success(self,'添加成功')
    return render(self,'home.html')

def view_list(self,list1_id):
    try:
        list_ = List.objects.get(id=list1_id)
    except List.DoesNotExist:
        raise Http404("HTTP Status 404 - Not Found")  
    #aa1=Item.objects.filter(list=list_)
    #aa1 = Item.objects.all()
    #return render(self,'list.html',{'test':aa1})
    return render(self,'list.html',{'list':list_})

def new_list(self):
    #aa1 = Item.objects.all()
    list_ = List.objects.create()
    Item.objects.create(text=self.POST['item_text'],list = list_)
    #return redirect('/lists/the-only-list-in-the-world/')
    return redirect(f'/lists/{list_.id}/')
    #return render(self,'list.html',{'items':aa1})
    
    
def add_item(self,list1_id):
    list_ = List.objects.get(id=list1_id) 
    Item.objects.create(text=self.POST['item_text'],list=list_)
    #return render(self,'list.html',{'list':list_})
    return redirect(f'/lists/{list_.id}/')
    
def other_list(self,list1_id):
    list_ = List.objects.get(id=list1_id) 
    Item.objects.create(text=self.POST['item_text'],list=list_)
    #aa1 = Item.objects.filter(list=list_)
    #list_ = List.objects.create()
    return render(self,'list.html',{'list':list_})
    #return render(self,'list.html',{'test':aa1})
    