from django import forms
from notes.models import Note

class NoteForm(forms.ModelForm):
    
    class Meta: 
        model = Note
        fields = ['title', 'description']

class SearchForm(forms.Form): 
    search_text = forms.CharField(label="Search Text", max_length=100)