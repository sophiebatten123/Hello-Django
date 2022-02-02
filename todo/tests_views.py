'''
        These tests enusre that the views.py file is correctly
        working and producing the desired effects. We use the
        CRUD operations from Django.
'''
from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    '''
        This class groups together the 6 main tests within the
        views.py file.
    '''

    # These test whether you are able to access the pages and if these
    # work correctly

    def test_get_todo_list(self):
        '''
        This tests that we are able to access the todo list page.
        The response code 200 means that we have accessed the
        HTTP response.
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        '''
        This tests that we are able to access the add item page.
        '''
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        '''
        This tests that we are able to access the edit item page.
        Template literals are used as the item id will vary.
        '''
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # These test the 3 functions to add, edit and delete the items

    def test_can_add_item(self):
        '''
        This tests that we are able to add an item. We create an
        instance of this within the response and then check it
        redirects to the page as this shows it is sucessful.
        '''
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        '''
        This tests that we are able to delete an item. We can
        ensure that it works by testing the length of the existing
        items has changed.
        '''
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        '''
        This tests that we are able to toggle an item
        '''
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
