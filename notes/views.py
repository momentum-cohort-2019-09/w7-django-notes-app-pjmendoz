from django.shortcuts import render
from notes.data import NOTES
from notes.models import Note

# Create your views here.
def notes_view(request): 
    return render(request, "notes/notes_list.html", {
        "notes": NOTES,
    })

def notes_detail(request, id):
    note = NOTES[id]
    return render(request, "notes/notes_detail.html", {"note": note})