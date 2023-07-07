from django import forms

class createNewTask(forms.Form):
    tittle = forms.CharField(label="titulo de tarea", max_length=200)
    description = forms.CharField(label="descripcion", widget=forms.Textarea, required=False)
    
class createNewProject(forms.Form):
    name = forms.CharField(label="nombre proyecto", max_length=30)
    