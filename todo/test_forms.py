'''
        These tests ensure that the forms.py file is
        working correctly using the CRUD django functions.
'''
from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    '''
        Here we group together the tests for the forms within
        a class which inherits the TestCase from django.
    '''

    def test_item_name_is_required(self):
        '''
        This is testing that a name is required on the form.
        If not it is producing an error message.
        '''
        form = ItemForm({'name': ' '})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        '''
        This is stating that the done field isnt required.
        It is making sure it is set to false by default.
        '''
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        '''
        This is ensuring that only the name and the done fields
        are being displayed to the user.
        '''
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
