from django import forms

from .models import VolLoc
from location_picker.fields import LocationField


class VolLocCreationForm(forms.ModelForm):

    date_end = forms.DateField(widget=forms.SelectDateWidget)
    date_start = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = VolLoc
        fields = [
        'name',
        'contact_email',
        'contact_phone',
        'location',
        'desc',
        'date_start',
        'date_end'
        ]
        widgets = {
        'desc' : forms.Textarea(attrs={'rows': 2, 'cols': 40})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Add A Name'
        self.fields['contact_email'].widget.attrs['placeholder'] = 'Email'
        self.fields['contact_phone'].widget.attrs['placeholder'] = 'Phone'
        self.fields['desc'].widget.attrs['placeholder'] = 'Description'
        self.fields['date_end'].widget.attrs['placeholder'] = 'Valid Till'
        self.fields['date_start'].widget.attrs['placeholder'] = 'Starts'
