from django.test import TestCase
from lists.forms import (
    DUPLICATE_ITEM_ERROR,EMPTY_ITEM_ERROR,
    ExistingListItemForms,ItemForm
)
from lists.models import Item,List


class ItemFormTest(TestCase):

    def test_from_renders_item_text_input(self):
        form = ItemForm()
        print(form.as_p())
        
    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"',form.as_p())
        self.assertIn('class="form-control input-lg"',form.as_p())
        
    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text':''})
        #form返回值
        status = form.is_valid()
        self.assertFalse(form.is_valid())
        #error返回值
        msg = form.errors['text']
        #print(msg)
        self.assertEqual(msg,[EMPTY_ITEM_ERROR])
        
    def test_form_save_handles_saving_to_a_list(self):
        list1 = List.objects.create()
        form = ItemForm(data={'text':'do me'})
        new_item = form.save(for_list=list1)
        self.assertEqual(new_item,Item.objects.first())
        self.assertEqual(new_item.text,'do me')
        self.assertEqual(new_item.list,list1)
        
class ExistingListItemFormTest(TestCase):
    
    def test_form_renders_item_text_input(self):
        list1 = List.objects.create()
        form = ExistingListItemForms(for_list=list1)
        self.assertIn('placeholder="Enter a to-do item"',form.as_p())
    
    def test_form_validation_for_blank_items(self):
        list1 = List.objects.create()
        form = ExistingListItemForms(for_list=list1,data={'text':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])
    
    def test_form_validation_for_duplicate_items(self):
        list1 = List.objects.create()
        Item.objects.create(list=list1, text='no twins!')
        form = ExistingListItemForms(for_list=list1, data={'text': 'no twins!'})
        status = form.is_valid()
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])
        
    def test_form_save(self):
        list1 = List.objects.create()
        form =  ExistingListItemForms(for_list=list1, data={'text':'hi'})
        new_item = form.save(for_list=list1)
        self.assertEqual(new_item, Item.objects.all()[0])
        
'''    
class Teststr(TestCase):

    def __init__(self, new_name, new_job):
        self.name = new_name
        self.job = new_job
    
    def __str__(self):
        return "名字是%s,职业是%s。" %(self.name,self.job)
    
    def eat(self):
        print("%s在吃东西..." %self.name)
xm = Teststr('xiaoming', 'Teacher')
print(xm)
xm.eat()
 '''
