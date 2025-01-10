from rest_framework.decorators import action
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
# tasks/views.py
from django.http import HttpResponse

def favicon_view(request):
    return HttpResponse(status=204)  # No Content

def home_view(request):
    return HttpResponse("<h1>Welcome to the Task Management API</h1>")

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    # Define the queryset attribute
    queryset = Task.objects.all()  # This will be overridden in get_queryset

    def get_queryset(self):
        # Override to return only tasks for the authenticated user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 'Completed':
            return Response({"detail": "Cannot edit a completed task."}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 'Completed':
            return Response({"detail": "Cannot edit a completed task."}, status=status.HTTP_400_BAD_REQUEST)
        return super().partial_update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'Completed'
        task.completed_at = timezone.now()
        task.save()
        return Response(TaskSerializer(task).data)
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('task-list')  # Redirect to task list or another page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form}) 

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('task-list')  # Redirect to task list or another page
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html') 
 