from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(label="Note Title", max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
    