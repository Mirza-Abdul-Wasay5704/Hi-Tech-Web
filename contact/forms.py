from django import forms
from .models import Contact, Quote
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            'phone',
            'message',
            Submit('submit', 'Send Message', css_class='btn btn-primary')
        )

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'email', 'phone', 'service_type', 'details']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-3'),
                Column('email', css_class='form-group col-md-6 mb-3'),
            ),
            Row(
                Column('phone', css_class='form-group col-md-6 mb-3'),
                Column('service_type', css_class='form-group col-md-6 mb-3'),
            ),
            'details',
            Submit('submit', 'Request Quote', css_class='btn btn-primary')
        )
