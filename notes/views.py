from django.shortcuts import render, redirect
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import NotesForm
from .models import Notes
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

"""class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    success_url = '/smart/notes'"""


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

    """def URLView(request):
        return redirect("{% url 'notes.list' %}")"""


# Creating a Class Based View for the Notes List Views
class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()


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
