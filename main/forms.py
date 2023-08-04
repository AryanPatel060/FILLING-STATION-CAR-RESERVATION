from django import forms
from .models import BookingSlot

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSlot
        fields = ['start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
