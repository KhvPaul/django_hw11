from datetime import timedelta

from django import forms
from django.utils import timezone


class ReminderForm(forms.Form):
    subject = forms.EmailField(label='Recipient email', help_text="Can't ends with 'test.com'")
    text = forms.CharField(label='Text', max_length=200)
    date_time = forms.DateTimeField(label='DateTime')

    def clean_date_time(self):
        date_time = self.cleaned_data.get('date_time') - timedelta(hours=2) + timedelta(milliseconds=1)
        # print(f'{timezone.now()} > {date_time}', timezone.now() > date_time)
        # print(f'{date_time} > {timezone.now() + timedelta(days=2)}', date_time > timezone.now() + timedelta(days=2))

        if timezone.now() > date_time:
            raise forms.ValidationError("now < input")

        if date_time > timezone.now() + timedelta(days=2):
            raise forms.ValidationError("input < now + 2 days")

        return date_time
