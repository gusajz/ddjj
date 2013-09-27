from django import forms
from .models import Document, Affidavit


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['notes']


class AffidavitForm(forms.ModelForm):

    class Meta:
        model = Affidavit
