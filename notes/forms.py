from django import forms
from notes.models import Note

class NoteForm(forms.ModelForm):
    
    class Meta: 
        model = Note
        fields = ['title', 'description']

class SearchForm(forms.Form): 
    q=forms.CharField(label='search', max_length=50)