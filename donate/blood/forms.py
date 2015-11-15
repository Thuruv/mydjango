from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from .models import Details, Feedback
from crispy_forms.bootstrap import TabHolder, Tab
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class AddmeForm(forms.ModelForm):
    class Meta:
        model = Details
        exclude = ['']

"""Forms for the ``feedback_form`` app."""

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('email', 'message')
