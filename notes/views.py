from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from notes.forms import NoteForm, SearchForm
from django.db.models import Q

# Create your views here.
def notes_list(request): 
    notes = Note.objects.all()
    return render(request, "notes/notes_list.html", {
        "notes": notes,
    })

def notes_detail(request, pk):
    note = Note.objects.get(id=pk)
    return render(request, "notes/notes_detail.html", {"note": note})

def notes_new(request):
    if request.method == "POST": 
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('notes_list')
    else: 
        form = NoteForm()    
    return render (request, "notes/notes_new.html", {"form": form})

def notes_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(instance=note, data=request.POST)
        #the model that you are going to be working on this form is that you will update this particular instance
        if form.is_valid():
            note = form.save()
            return redirect(to='notes_detail', pk=note.pk)
    else: 
        form = NoteForm(instance=note)    
    return render(request, 'notes/notes_edit.html', {
        "note": note,
        "form": form, 
    })

def notes_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect(to='notes_list')
    return render(request, 'notes/notes_delete.html',{"note": note})

def search_notes(request):
    search_notes = []
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            notes = Note.objects.all()
            data = request.POST.copy()
            for note in notes:
                if data.get('search_text') in note.title:
                    search_notes.append(note)
            return render(request, 'notes/search_results.html', {'notes': search_notes})   
    else: 
        form = SearchForm()  
    return render(request, 'notes/search_notes.html',{'form': form })           


def sort_notes(request):
    pass
