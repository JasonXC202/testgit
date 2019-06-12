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

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #staging_server = os.environ.get('STAGING_SERVER')
        #if staging_server:
          #  self.live_server_url = 'http://' + staging_server
        
    def tearDown(self):
        self.browser.quit()
        
    def wait_for_row_in_list_table(self,column_text):
        start_time = time.time()
        #print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                trlist = table.find_elements_by_id('tr1')
                tdlist = table.find_elements_by_tag_name('td')
                self.assertIn(column_text,[row.text for row in tdlist])
                return
            except (AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
