from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label="Description")
    detailed_description = forms.CharField(max_length=3000, required=True, label="Detailed description",
                                           widget=widgets.Textarea(attrs={"rows":5 , "cols":50}))
    status = forms.CharField(required=True, max_length=15, label="Status",
                          widget=widgets.Select)
    create_until = forms.CharField(label="Create until",
                                   widget=widgets.SelectDateWidget)