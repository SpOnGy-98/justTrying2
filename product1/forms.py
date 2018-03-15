from django import forms

class CommentForms(forms.Form):
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'placeholder': 'Name',
                                      'style': 'border: 0px;'}))
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Comment',
               'style': 'border: 0px;'}))
