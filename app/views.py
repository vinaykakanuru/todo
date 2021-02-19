from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import ToDo
from app.forms import ToDoForm
# Create your views here.


def home(request):
    todo_list = ToDo.objects.all()
    form = ToDoForm()
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'home.html', context=context)


def add_todo(request):
    if request.method == 'POST':
        # save the todo
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data.get('todo_text')
            ToDo.objects.create(name=todo_text)

    return redirect('home')


def delete_todo(request, id):
    if request.method == 'POST':
        todo_obj = ToDo.objects.get(pk=id)
        todo_obj.delete()

    return redirect('home')


def edit_todo(request, id):
    todo_obj = ToDo.objects.get(pk=id)

    if request.method == 'POST':
        form = ToDoForm(request.POST, initial={
                        'todo_text': todo_obj.name})
        if form.is_valid():
            todo_obj.name = form.cleaned_data.get('todo_text')
            todo_obj.save()
            return redirect('home')

    form = ToDoForm(initial={'todo_text': todo_obj.name})
    context = {'form': form, 'todo_obj': todo_obj}
    return render(request, 'edit.html', context)
