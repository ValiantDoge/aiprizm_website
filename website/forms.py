from django import forms
from .models import Contact
from django.forms import Textarea

# Create your forms here.

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': Textarea(attrs={'cols': 80, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label.title()