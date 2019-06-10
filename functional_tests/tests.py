from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lists.models import Item
import time
from selenium.common.exceptions import WebDriverException
import unittest
MAX_WAIT = 5

class NewVistorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
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
                
    def show_table_cell_value(self):
        table = self.browser.find_element_by_id('id_list_table')
        trlist = table.find_elements_by_id('tr1') 
        for tr in trlist:
            text=tr.find_elements_by_tag_name("td")[1].text
            print(text)
    
    def test_layout_and_styling(self):
        #访问首页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)
        
        #输入框居中显示
        inputbox = self.browser.find_element_by_id('id_new1')
        print(inputbox.location['x'])
        print(inputbox.location['y'])
        print(inputbox.size['width'])
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2 ,512,delta=10
        )
    '''           
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        data = ["1:Buy peacock feathers","2:Use peacock feathers to make a fly"]
        for i in range(0,len(data)):
            inputbox = self.browser.find_element_by_id('id_new1')
            self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
            inputbox.send_keys(data[i])
            inputbox.send_keys(Keys.ENTER)
            time.sleep(2)
            self.wait_for_row_in_list_table(data[i])
        #self.show_table_cell_value()
        edith_list_url = self.browser.current_url
        print(edith_list_url)
    
    def test_multiple_user_can_start_lists_at_differenet_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new1')
        inputbox.send_keys("3:Buy peacock feathers1")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("3:Buy peacock feathers1")
        edith_list_url = self.browser.current_url
        print(edith_list_url)
        self.assertRegex(edith_list_url,'/lists/.+')
        time.sleep(3)
        #新用户访问
        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers1', page_text)
        self.assertNotIn('Use peacock feathers to make a fly', page_text)
        time.sleep(3)
        #新用户输入
        inputbox = self.browser.find_element_by_id('id_new1')
        inputbox.send_keys('4:Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('4:Buy milk')
        time.sleep(3)
        #获得唯一地址
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        #提交清单判断
        page_text1 = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers1', page_text1)
        self.assertIn('Buy milk', page_text1)
        
    table = self.browser.find_element_by_id('id_list_table')
        trlist = self.browser.find_elements_by_tag_name('tr')
        for row in trlist:
            tdlist = self.browser.find_elements_by_tag_name('td')
            for col in tdlist:
                print("column:" + column_test)
                print("col:" + col.text)

        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows),
            f"New to-do item did not appear in table.Content were:\n{table.text}"
            )
        
        self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )
        time.sleep(3)
        '''
        #self.fail('Finish the test!')
#print(__name__)
#if __name__ =='__main__':
   # unittest.main(warnings='ignore')
   
