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
        self.browser.find_element_by_id('id_new1').send_keys(Keys.ENTER)
        self.wait_for(lambda: self.assertEqual(
             self.browser.find_element_by_css_selector('.has-error').text,
             "You can't hava an empty list item"
        ))
        self.browser.find_element_by_id('id_new1').send_keys('Buy milk')
        self.browser.find_element_by_id('id_new1').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('Buy milk')
        #self.fail('finish this test!')
    

   
