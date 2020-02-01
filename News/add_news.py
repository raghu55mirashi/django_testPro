from django import forms


class AddNews(forms.Form):
    author = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=100)

