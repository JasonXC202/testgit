from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(self):
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    return render(self,'home.html')
#home_page = None
