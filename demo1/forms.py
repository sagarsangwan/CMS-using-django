from django import forms
from .models import users_form
from django.core.exceptions import ValidationError


class form_users_form(forms.ModelForm):
    class Meta:
        model = users_form
        fields = ['user_name', 'user_email', 'user_password',
                  'confirm_password', 'user_address']

    def clean(self):
        print(self.cleaned_data)
        return None

        # widgets = {
        #     'user_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'user_email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'user_password': forms.TextInput(attrs={'class': 'form-control'}),
        #     'confirm_password': forms.TextInput(attrs={'class': 'form-control'}),
        #     'user_address': forms.TextInput(attrs={'class': 'form-control'}),
        # }
