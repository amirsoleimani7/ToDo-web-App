from django.shortcuts import render , redirect
from django.contrib import messages

from .forms import ToDoForm
from .models import Todo


def index(request):
    
    item_list = Todo.objects.order_by("-date")
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo")
    form = ToDoForm()



    conetxt = {
        "forms" : form ,
        "list" : item_list , 
        "title" :  "TODO LIST"
    }

    return render(request , "todo_app/index.html" , conetxt)



def remove(request , item_id):
    item = Todo.objects.get(id = item_id)
    item.delete()
    messages.info(request , "item removed !!")
    return redirect('todo')

