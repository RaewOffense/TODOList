from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import TodoList 
from .forms import TodoForm

# Create your views here.


def add_task(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm()
    return render(request,"add_task.html",{"form":form})


# def add_task(request):
#     task = start_date = end_date = completed = None  
#     if request.method =="POST":
#         task = request.POST.get('task')
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')
#         completed = request.POST.get('completed')=="True"
#     if task and start_date and end_date:
#         new_todolist = TodoList(
#             task = task,
#             start_date = start_date,
#             end_date = end_date,
#             completed =completed
#         )

#         new_todolist.save()
#         return redirect("/")

#     return render(request,"add_task.html")


def read_task(request):
    tasks = TodoList.objects.all().order_by('-id')
    return render(request,"index.html",{'tasks': tasks})


def update_task(request,task_id):
    update_form = get_object_or_404(TodoList,id=task_id)
    if request.method == "POST":
        form = TodoForm(request.POST,instance = update_form)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TodoForm(instance = update_form)
    return render(request, 'updateTask.html', {'form':form})


def delete_task(request,task_id):
    delete_task = TodoList.objects.get(id=task_id)
    delete_task.delete()
    return redirect('/')
    


