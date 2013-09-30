# coding=utf-8

from django import forms

from .models import Document, Affidavit


class DocumentForm(forms.ModelForm):
    # el archivo debería ser read only si es update.
    pass


class AffidavitForm(forms.ModelForm):

    class Meta:
        model = Affidavit
