from django.test import TestCase
from lists.forms import ItemForm,EMPTY_ITEM_ERRORS


class ItemFormTest(TestCase):

    def test_from_renders_item_text_input(self):
        form = ItemForm()
        form.as_p()
        
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
        self.assertEqual(
            msg,
            [EMPTY_ITEM_ERRORS]
        )
        
        
    
    
    
