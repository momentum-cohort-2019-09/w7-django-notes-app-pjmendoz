from django.shortcuts import render, redirect
from notes.models import Note
from notes.forms import NoteForm
# Create your views here.
def notes_view(request): 
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {
        "notes": notes,
    })

def notes_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, "notes/notes_detail.html", {"note": note})

def new_note(request):
    if request.method == "POST": 
        form = NoteForm(request.POST)
        if form.is_valid():
            note = Note()
            note.title = form.cleaned_data['title']
            note.description = form.cleaned_data['description']
            
            note.save()
            return redirect(to='notes_view')
    else: 
        form = NoteForm()    
    return render (request, "notes/new_note.html", {"form": form})