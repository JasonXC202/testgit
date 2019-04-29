from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(self):
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    #if self.method == 'POST':
     #   return HttpResponse(self.POST['item_text'])
    return render(self,'home.html',{'aabb':self.POST.get('item_text','')})
#home_page = None
