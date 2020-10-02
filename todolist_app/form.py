# when we are dealing with forms, use this
from django import forms
from todolist_app.models import TaskList

class TaskForm(forms.ModelForm):
    class Meta:
        model =  TaskList
        fields  = ['task', 'done']

