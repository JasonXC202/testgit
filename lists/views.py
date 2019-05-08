from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(self):
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    if self.method == 'POST':
        new_item_text = self.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    #else:
        #new_item_text = ""
    aa = Item.objects.all()
    return render(self,'home.html',{'items':aa})
#home_page = None
