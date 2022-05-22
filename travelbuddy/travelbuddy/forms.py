from django import forms
from .models import MapModel, ChecklistModel, JournalModel


# pChecklist form
class MapModelForm(forms.ModelForm):
    location_points = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = MapModel
        fields = ('location_points',)    # always need to add comma after the field esp when there's one field.


class ChecklistModelForm(forms.ModelForm):
    class Meta:
        model = ChecklistModel
        fields = ('checklist',)


# Journal form
class JournalModelForm(forms.ModelForm):
    journal = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add your journal here', 'rows': 4}
                                                               ))

    class Meta:
        model = JournalModel
        fields = ('journal',)



