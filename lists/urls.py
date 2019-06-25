"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from lists import views
#from django.contrib import admin

urlpatterns = [
    url(r'^new$',views.new_list,name='new_list1'),
    url(r'^(\d+)/other$',views.other_list,name='new_list2'),
    url(r'^the-only-list-in-the-world/$',views.view_list,name='view_list2'),
    url(r'^(\d+)/$',views.view_list,name='view_list1'),
    #url(r'^(\d+)/add_item$',views.add_item,name='add_item'),
    url(r'^test$',views.get_html,name='home1'),
]
