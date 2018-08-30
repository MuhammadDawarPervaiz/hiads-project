from django import forms
from .models import Subscribe

class SubscriberForm(forms.ModelForm):
    email = forms.EmailField(widget = forms.EmailInput(
        attrs = {
            'class': 'subx',
            'placeholder':'Your Email',
            'type':'email',
        }
    ))

    class Meta:
        model = Subscribe
        fields = ('email',)

class ContactForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput(
        attrs = {
            'class': 'small-input',
            'placeholder':'Your Name',
            'type':'text',
        }
    ))
    email = forms.EmailField(widget = forms.EmailInput(
        attrs = {
            'class': 'small-input',
            'placeholder':'Email Here',
            'type':'email',
        }
    ))
    message = forms.CharField(widget = forms.Textarea(
        attrs = {
            'class': 'message',
            'placeholder':'Message',
            'type':'email',
            'cols':'30',
            'rows':'3',
        }
    ))
