from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
    def check_for_row_in_list_table(self,row_test):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_test,[row.text for row in rows])
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        data = ["1:Buy peacock feathers","2:Use peacock feathers to make a fly"]
        for i in range(0,len(data)):
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
            inputbox.send_keys(data[i])
            inputbox.send_keys(Keys.ENTER)
            time.sleep(3)
            self.check_for_row_in_list_table(data[i])
    #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
        #text=tr.find_elements_by_tag_name("td")[0].text
        #print(text)
        '''
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
if __name__ =='__main__':
    unittest.main(warnings='ignore')

