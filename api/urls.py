from django.urls import path

from . import views

urlpatterns = [
    path('snippet', views.snippet_list, name='snippet'),
    path('create-snippet', views.create_snippet, name='create-snippet'),
]
