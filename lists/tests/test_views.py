from django.urls import resolve
from django.test import TestCase,LiveServerTestCase
from lists.views import home_page,get_html
from django.http import HttpRequest
from lists.models import Item,List
from lists.forms import ItemForm,EMPTY_ITEM_ERRORS
from django.contrib import messages
from selenium import webdriver
import time
from  django.utils.html import escape

# Create your tests here.
class ListViewTest(TestCase):

	def test_displays_all_list_items(self):
		list1 = List.objects.create()
		Item.objects.create(text='itemey 1',list=list1)
		Item.objects.create(text='itemey 2',list=list1)
		
		response = self.client.get(f'/lists/test')
		#print(response.content.decode())
		self.assertContains(response,'itemey 1')
		self.assertContains(response,'itemey 2')
	'''	   
	def test_url_resolve(self):
		url =resolve('/2012/10')
		print(url.url_name)
		self.assertEqual(url.func, home_page1)
	'''	  
	def test_uses_list_template(self):
		list1 = List.objects.create()
		#response = self.client.get('/lists/the-only-list-in-the-world/')
		response = self.client.get(f'/lists/{list1.id}/')
		self.assertTemplateUsed(response,'list.html')
	
	def test_displays_only_items_for_that_list(self):
		correct_list = List.objects.create()
		Item.objects.create(text='itemey 1',list = correct_list)
		Item.objects.create(text='itemey 2',list = correct_list)
		
		other_list = List.objects.create()
		Item.objects.create(text='other list item 1',list = other_list)
		Item.objects.create(text='other list item 2',list = other_list)
		
		#Item.objects.all()
		#response = self.client.get(f'/lists/the-only-list-in-the-world/')
		response = self.client.get(f'/lists/{correct_list.id}/')
		#print(response.content.decode())
		self.assertContains(response,'itemey 1')
		self.assertContains(response,'itemey 2')
		self.assertNotContains(response,'other list item 1')
		self.assertNotContains(response,'other list item 2')
		
	def test_can_save_a_POST_request(self):
		response = self.client.post('/lists/new',data={'text':'A new list item'})
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text,'A new list item')
		#self.assertIn('A new list item',response.content.decode())
		#self.assertTemplateUsed(response,'home.html')
		
	def test_redirects_after_POST(self):
		response = self.client.post('/lists/new',data={'text':'A new list item'})
		new_list=List.objects.first()
		#self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
		self.assertRedirects(response, f'/lists/{new_list.id}/')
		#self.assertEqual(response.status_code,302)
		#self.assertEqual(response['location'],'/lists/the-only-list-in-the-world/')
		
	def test_can_save_a_POST_request_to_an_exist_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		
		response = self.client.post(f'/lists/{correct_list.id}/',
		data={'text':'A new item for an existing list'})
		
		#去除add_item
		#response1 = self.client.post(f'/lists/{correct_list.id}/add_item',
		#data={'text':'A new item for an existing list'})
		
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text,'A new item for an existing list')
		self.assertEqual(new_item.list,correct_list)
		
	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		
		response = self.client.post(f'/lists/{correct_list.id}/',
		data={'text':'A new item for an existing list'}
		)
		
		#去除add_item
		#response1 = self.client.post(f'/lists/{correct_list.id}/add_item',
		#data={'text':'A new item for an existing list'}
		#)
		
		self.assertRedirects(response, f'/lists/{correct_list.id}/')
		#response1 = self.client.get(f'/lists/{correct_list.id}/')
		#self.assertContains(response1,'A new item')
	'''
	#提交列表清单
	def test1_post_method(self):
		list1 = List.objects.create()
		response = self.client.post(f'/lists/{list1.id}/',data={'text':'12335'})
		self.assertContains(response,'12335')
		print("POST方法："+"\n"+response.content.decode())
	
	def test1_get_method(self):
		list1 = List.objects.create()
		Item.objects.create(text='item 1',list=list1)
		response = self.client.get(f'/lists/{list1.id}/')
		#response1 = response.context['list']
		#print(response.content.decode())
		self.assertContains(response,'item 1')
		#print("GET方法"+"\n"+response.content.decode()	
	'''
	
	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get(f'/lists/{correct_list.id}/')
		#print(response.context['list'])
		self.assertEqual(response.context['list'],correct_list)
		
	#测试项目过多，分解为3个，一个单元测试测试一件事
	'''
	def test_validation_errors_are_send_back_to_home_page(self):
		response = self.client.post(f'/lists/new',data={'text':''})
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'home.html')
		#print(response.content.decode())
		expected_error = escape("You can't have an empty list item")
		self.assertContains(response,expected_error)
	'''
	#验证错误，渲染首页模板
	def test_for_invalid_input_renders_home_template(self):
		response = self.client.post(f'/lists/new',data={'text':''})
		#print(response.status_code)
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'home.html')
	
	#验证错误，响应中包含错误信息
	def test_validation_errors_are_shown_on_home_page(self):
		response = self.client.post(f'/lists/new',data={'text':''})
		#print(response.content.decode())
		self.assertContains(response,escape(EMPTY_ITEM_ERRORS))
	
	#有验证错误，把表单对象传入模板
	def test_for_invalid_input_passes_form_to_template(self):
		response = self.client.post(f'/lists/new',data={'text':''})
		print(response.content.decode())
		self.assertIsInstance(response.context['form'],ItemForm)
	
	def test_invalid_list_items_arent_saved(self):
		response = self.client.post(f'/lists/new',data={'text':''})
		#print(response.content.decode())
		self.assertEqual(List.objects.count(),0)
		self.assertEqual(Item.objects.count(),0)
	
	#测试待办视图是否使用表单
	def test_displays_item_form(self):
		list1=List.objects.create()
		response=self.client.get(f'/lists/{list1.id}/')
		self.assertIsInstance(response.context['form'],ItemForm)
		self.assertContains(response,'name="text"')
	
	#分解测试，测试内容过多
	'''
	def test_validation_errors_end_up_on_lists_page(self):
		list1 = List.objects.create()
		response = self.client.post(f'/lists/{list1.id}/',data={'text':''})
		#print(response.content.decode())
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'list.html')
		expected_error = escape("You can't have an empty list item")
		self.assertContains(response,expected_error)
	'''
	
	#列表清单提交成功数据
	def post_valid_input(self):
		list1 = List.objects.create()
		response = self.client.post(f'/lists/{list1.id}/',data={'text':'test sucess value1'})
		self.assertEqual(response.status_code,200)
		return response
		
	#显示列表清单数据
	def show_list_value(self):
		self.post_valid_input()
		list1=List.objects.first()
		response1 = self.client.get(f'/lists/{list1.id}/')
		#print(response.content.decode())
		self.assertContains(response1,'4')
	 
	#列表清单提交空数据	   
	def post_invalid_input(self):
		list1 = List.objects.create()
		response = self.client.post(f'/lists/{list1.id}/',data={'text':''})
		return response
		 
	def test_for_invalid_input_nothng_saved_to_db(self):
		response = self.post_invalid_input()
		self.assertEqual(Item.objects.count(), 0)
		
	def test_for_invalid_input_renders_list_template(self):
		response = self.post_invalid_input()
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'list.html')
		
	def test_for_invalid_input_passes_form_to_template(self):
		response = self.post_invalid_input()
		self.assertIsInstance(response.context['form'], ItemForm)
		
	def test_for_invalid_input_shows_error_on_page(self):
		response = self.post_invalid_input()
		self.assertContains(response, escape(EMPTY_ITEM_ERRORS)) 
	
		
'''
class SmokeTest(TestCase):
	def test_bad_maths(self):
		self.assertEqual(1+1,3)

class ItemModelTest(TestCase):
	def test_saving_and_retrieving_items(self):
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.save()
		
		second_item = Item()
		second_item.text = 'Item the second'
		second_item.save()
		
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(),2)
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text,'The first (ever) list item')
		self.assertEqual(second_saved_item.text,'Item the second')
'''
class HomePageTest(TestCase):
	def test_uses_home_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'home.html')
		#messages.success(self,'添加成功')
		
	#def test_only_saves_item_when_necessary(self):
	  #	 response1=self.client.get('/')
		#self.assertEqual(Item.objects.count(),0)
		
	#验证表单类型是否正确	  
	def test_home_page_uses_item_form(self):
		response = self.client.get('/')
		#print(response.context['form'])
		self.assertIsInstance(response.context['form'],ItemForm)
'''	 
class ListAndItemModelsTest(TestCase):
	def test_saving_and_retrieving_items(self):
		list_ = List()
		list_.save()
		
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()
		
		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()
		
		saved_list = List.objects.first()
		self.assertEqual(saved_list,list_)
		
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(),2)
		
		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text,'The first (ever) list item')
		self.assertEqual(first_saved_item.list,list_)
		self.assertEqual(second_saved_item.text,'Item the second')
		self.assertEqual(second_saved_item.list,list_)

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func,home_page)
	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>',html)
		self.assertTrue(html.endswith('</html>'))
	def test_home_page_returns_correct_html1(self):
		response = self.client.get('/')
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>',html)
		self.assertTrue(html.endswith('</html>'))
		self.assertTemplateUsed(response,'home.html')
'''