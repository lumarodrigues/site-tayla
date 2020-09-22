from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=100, required=True)
    subject = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea)
