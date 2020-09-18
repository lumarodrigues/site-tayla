from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea)
