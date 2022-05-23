from django import forms
from .models import MapModel


# pChecklist form
class MapModelForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    orig_loc = forms.CharField(max_length=50)
    dest_loc = forms.CharField(max_length=50)
    waypoints = forms.CharField(widget=forms.Textarea(attrs={'rows': 15}))
    check_item = forms.CharField(widget=forms.Textarea(attrs={'rows': 20}))
    journal = forms.CharField(widget=forms.Textarea(attrs={'rows': 20}))

    class Meta:
        model = MapModel
        fields = ['title', 'orig_loc', 'dest_loc', 'waypoints', 'check_item', 'journal']    # always need to add comma after the field esp when there's one field.


# class ChecklistModelForm(forms.ModelForm):
#     class Meta:
#         model = ChecklistModel
#         fields = ('checklist',)
#
#
# # Journal form
# class JournalModelForm(forms.ModelForm):
#     journal = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add your journal here', 'rows': 4}
#                                                                ))
#
#     class Meta:
#         model = JournalModel
#         fields = ('journal',)



