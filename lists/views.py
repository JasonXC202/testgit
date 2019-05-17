from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item,List
from django.contrib import messages

# Create your views here.
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

def view_list(self):
    aa1 = Item.objects.all()
    return render(self,'list.html',{'items':aa1})

def new_list(self):
    #aa1 = Item.objects.all()
    list_ = List.objects.create()
    Item.objects.create(text=self.POST['item_text'],list = list_)
    return redirect('/lists/the-only-list-in-the-world/')
    #return render(self,'list.html',{'items':aa1})