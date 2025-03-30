from django.shortcuts import render, redirect
from django.conf import settings
import requests
from django.contrib import messages

def todo_list(request):
    try:
        response = requests.get(f"{settings.API_BASE_URL}/todos")
        todos = response.json()
        return render(request, 'todo_app/todo_list.html', {'todos': todos})
    except requests.RequestException as e:
        messages.error(request, f'Error connecting to API: {str(e)}')
        return render(request, 'todo_app/todo_list.html', {'todos': []})

def add_todo(request):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'completed': False
        }
        try:
            response = requests.post(f"{settings.API_BASE_URL}/todos", json=data)
            if response.status_code == 201:
                messages.success(request, 'Todo added successfully!')
            else:
                messages.error(request, 'Failed to add todo.')
        except requests.RequestException as e:
            messages.error(request, f'Error connecting to API: {str(e)}')
        return redirect('todo_app:todo_list')
    return render(request, 'todo_app/add_todo.html')

def update_todo(request, todo_id):
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'completed': request.POST.get('completed') == 'on'
        }
        try:
            response = requests.put(f"{settings.API_BASE_URL}/todos/{todo_id}", json=data)
            if response.status_code == 200:
                messages.success(request, 'Todo updated successfully!')
            else:
                messages.error(request, 'Failed to update todo.')
        except requests.RequestException as e:
            messages.error(request, f'Error connecting to API: {str(e)}')
        return redirect('todo_app:todo_list')
    
    try:
        response = requests.get(f"{settings.API_BASE_URL}/todos/{todo_id}")
        todo = response.json()
        return render(request, 'todo_app/update_todo.html', {'todo': todo})
    except requests.RequestException as e:
        messages.error(request, f'Error connecting to API: {str(e)}')
        return redirect('todo_app:todo_list')

def delete_todo(request, todo_id):
    if request.method == 'POST':
        try:
            response = requests.delete(f"{settings.API_BASE_URL}/todos/{todo_id}")
            if response.status_code == 204:
                messages.success(request, 'Todo deleted successfully!')
            else:
                messages.error(request, 'Failed to delete todo.')
        except requests.RequestException as e:
            messages.error(request, f'Error connecting to API: {str(e)}')
    return redirect('todo_app:todo_list')
