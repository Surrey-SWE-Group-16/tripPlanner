from django import forms
from .models import PostModel, Comment

# post create form
class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')

# post edit form
class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content')

# comment create form

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Add comment here', 'rows': 2}))
    class Meta:
        model = Comment
        fields = ('content',)



