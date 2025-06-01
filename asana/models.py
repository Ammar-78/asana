# from django.db import models

# # Create your models here.

# from django.db import models

# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# from django.db import models
# from django.contrib.auth.models import User

# class Task(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     due_date = models.DateField(null=True, blank=True)
#     completed = models.BooleanField(default=False)
#     assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# 25-00-2025

# asana/models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


