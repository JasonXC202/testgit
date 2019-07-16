from django.test import TestCase
from lists.forms import ItemForm,EMPTY_ITEM_ERRORS
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
		#print(status)
		self.assertFalse(form.is_valid())
		#error返回值
		msg = form.errors['text']
		#print(msg)
		self.assertEqual(msg,[EMPTY_ITEM_ERRORS])
		
	def test_form_save_handles_saving_to_a_list(self):
		list1 = List.objects.create()
		form = ItemForm(data={'text':'do me'})
		new_item = form.save(for_list=list1)
		self.assertEqual(new_item,Item.objects.first())
		self.assertEqual(new_item.text,'do me')
		self.assertEqual(new_item.list,list1)
	
	
	
