from django import forms
from .models import Invitation, CustomTemplate

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['p_from','p_to','place','invitation_date','description','template','is_formal']
        labels = {
            "p_from": "From",
            "p_to": "To"
        }

class InvitationWithCustomForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['p_from','p_to','place','invitation_date','description','is_formal']
        labels = {
            "p_from": "From",
            "p_to": "To"
        }

class CustomTemplateForm(forms.ModelForm):
    class Meta:
        model = CustomTemplate
        fields = ['title','description', 'docfile']