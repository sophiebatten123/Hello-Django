'''
These tests will help to check the todo items will be
created with a done status of false.
'''
from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    '''
        Groups together the models.
    '''

    def test_done_defaults_to_false(self):
        '''
            This test will check is the done status is set
            to false by default
        '''
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        '''
            This will test the the string will return a
            name.
        '''
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
