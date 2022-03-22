from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView

from .models import Notes


class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'


# Creating a Class Based View for the Notes List Views
class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"


"""Also, looking at the Workings of Class Based Views"""

# Create your views here.
# This is the Old Function EndPoint Created for Notes List View
"""def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':all_notes})"""

"""def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Notes Doesn't Exist")
    return render(request, 'notes/notes_detail.html', {'note':note})"""
