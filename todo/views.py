'''
        Within the views file this is what is producing the
        response from the user. Here we connect the database
        and static HTML
'''
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create your views here.
def get_todo_list(request):
    '''
        This initially renders the HTML page todo list and
        creates a connection to the data base with the clss
        of Item.
    '''
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    '''
        This will allow the user to add an item to the
        database and after this has been done redirects them
        back to the todo list page.
    '''
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    '''
        This will allow the user to edit an item to the
        database and after this has been done redirects them
        back to the todo list page.
    '''
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    '''
        This will allow the user to toggle an item to the
        database and after this has been done redirects them
        back to the todo list page.
    '''
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    '''
        This will allow the user to delete an item to the
        database and after this has been done redirects them
        back to the todo list page.
    '''
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
