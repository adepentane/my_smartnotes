# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),

]
