from django import forms
from allauth.account.forms import SignupForm
from .models import User


class UserProfile(forms.Form):
    class Meta:
        model = User
        fields = "__all__"

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom classes to fields as required
        self.fields['email'].widget.attrs.update({'class': 'w-full py-2.5 px-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['password1'].widget.attrs.update({'class': 'w-full py-2.5 px-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
        self.fields['password2'].widget.attrs.update({'class': 'w-full py-2.5 px-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'})
