#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lists.models import Item
import time
from selenium.common.exceptions import WebDriverException
import unittest,os
from unittest import skip
MAX_WAIT = 5
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        #访问首页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)
        time.sleep(10)
        
        #输入框居中显示
        inputbox = self.browser.find_element_by_id('id_new1')
        #print(inputbox.location['x'])
        #print(inputbox.location['y'])
        #print(inputbox.size['width'])
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2 ,512,delta=10
        )
        
