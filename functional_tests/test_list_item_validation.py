#from django.test import LiveServerTestCase
#from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from lists.models import Item
import time
from selenium.common.exceptions import WebDriverException
#import unittest,os
#from unittest import skip

from .base import FunctionalTest
class itemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self): 
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for(lambda: self.browser.find_element_by_css_selector(
			'#id_text:invalid'
		))
		self.get_item_input_box().send_keys('Buy milk')
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('Buy milk')
		#self.fail('finish this test!')
		
	def test_cannot_add_duplicate_items(self):
		#访问首页，新建一个清单
		self.browser.get(self.live_server_url)
		self.get_item_input_box().send_keys('Buy wellies')
		self.get_item_input_box().send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('Buy wellies')
		
		#输入重复数据
		self.get_item_input_box().send_keys('Buy wellies')
		self.get_item_input_box().send_keys(Keys.ENTER)
		
		#错误信息查看
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text,
			"You've alraady got this in your list"
		))
		
		
		
	
   