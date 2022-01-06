from django import forms


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label="Description")
    detailed_description = forms.TextField(max_length=3000, required=True, label="Detailed description")
    status = forms.CharField(max_length=15, required=True, label="Status")
    create_until = forms.DateField(label="Create until")