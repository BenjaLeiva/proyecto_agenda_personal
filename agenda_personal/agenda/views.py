from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskForm, UserSignupForm
from .models import Task
from .forms import TaskForm

@login_required 
def task_list(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('agenda:task_list') 
    else:
        form = TaskForm()
    
    all_tasks = Task.objects.filter(user=request.user).order_by('is_completed', 'due_date', 'created_at')
    
    paginator = Paginator(all_tasks, 8) 
    page = request.GET.get('page')
    
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    
    context = {
        'tasks': tasks, 
        'form': form,
        'page_title': 'Mi Agenda Personal',
    }
    return render(request, 'agenda/task_list.html', context)

@login_required
@require_POST
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user) 
    task.is_completed = not task.is_completed
    task.save()
    return redirect('agenda:task_list')

@login_required
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    return redirect('agenda:task_list')


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            return redirect('agenda:task_list')
    else:
        form = TaskForm(instance=task)
        
    context = {
        'task': task,
        'form': form,
        'page_title': f'Editar: {task.title[:20]}...',
    }
    return render(request, 'agenda/edit_task.html', context)

def signup(request):
    """Permite a los usuarios crear una nueva cuenta."""
    if request.user.is_authenticated:
        return redirect('agenda:task_list')

    if request.method == 'POST':
        form = UserSignupForm(request.POST) # <--- Usar UserSignupForm
        if form.is_valid():
            form.save()
            # Opcional: Mostrar mensaje de éxito
            return redirect('login') 
    else:
        form = UserSignupForm() # <--- Usar UserSignupForm
        
    context = {
        'form': form,
        'page_title': 'Crear Cuenta'
    }
    # Asegúrate de usar la ruta correcta a tu template (registro/signup.html)
    return render(request, 'registro/signup.html', context)