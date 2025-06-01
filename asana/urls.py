# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.task_list, name='task_list'),
# ]

# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.task_list, name='task_list'),

# ]


# asana/urls.py


from django.urls import path
from . import views

app_name = 'asana'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
]

