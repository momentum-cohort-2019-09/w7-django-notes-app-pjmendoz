from django.shortcuts import render
from notes.data import NOTES

# Create your views here.
def notes_view(request): 
    return render(request, "notes/notes_view.html", {
        "notes": NOTES,
    })