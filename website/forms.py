from pickle import FALSE
from django import forms
from website.models import Contact, Newsletter

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False


class NewsletterForm(forms.ModelForm):

    class Meta():
        model = Newsletter
        fields = '__all__'
