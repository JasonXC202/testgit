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
class itemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        self.fail('write me')
    

   
