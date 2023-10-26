from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'date_joined', 'date_expired']

    def clean(self):
        cleaned_data = super().clean()
        date_joined = cleaned_data.get('date_joined')
        date_expired = cleaned_data.get('date_expired')

        # Check if date_expired is earlier than date_joined
        if date_joined and date_expired and date_expired < date_joined:
            raise forms.ValidationError("Date expired cannot be earlier than date joined.")

        return cleaned_data