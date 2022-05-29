from django import forms
from django.forms import ModelForm
from .models import MapModel


# pChecklist form
class MapModelForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    orig_loc = forms.CharField(max_length=50)
    dest_loc = forms.CharField(max_length=50)
    waypoints = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 15}))
    check_item = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 20}))
    journal = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 20}))
    distance = forms.IntegerField()


    class Meta:
        model = MapModel
        fields = ('title', 'orig_loc', 'dest_loc', 'waypoints', 'check_item', 'journal', 'distance')    # always need to add comma after the field esp when there's one field.






