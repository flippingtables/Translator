__author__ = 'joannes'

from django import forms
from TranslatorManager.models import Client,ClientJob

class ClientForm(forms.ModelForm):
    clientName = forms.CharField(max_length=200, help_text="Please enter the client name.")
    clientContact = forms.CharField(max_length=200, help_text="Please enter the client contact.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Client
        fields = ["clientName", "clientContact"]


class AddJobForm(forms.ModelForm):
    ENGLISH = 'EN'
    FRENCH = 'FR'
    SPANISH = 'ES'
    LANGUAGES = (
        (ENGLISH, 'English'),
        (FRENCH, 'French'),
        (SPANISH, 'Spanish'),
    )
    TRANSLATION = 'Translation'
    REVIEW = 'Review'
    DTP = 'DTP'

    SERVICES = (
        (TRANSLATION, 'Translation'),
        (REVIEW, 'Review'),
        (DTP, 'DTP'),
    )
    #client = forms.IntegerField()
    #clientContact = forms.CharField(max_length=100)

    #clientName = forms.CharField(max_length=200, help_text="Please enter the client name.")
    clientContact = forms.CharField(max_length=200, help_text="Please enter the client contact.")

    languageFrom = forms.CharField(max_length=2)
    languageTarget = forms.CharField(max_length=2)
    description = forms.CharField(max_length=300)
    service = forms.CharField(max_length=20)
    deadLine = forms.DateTimeField()
    hours_Spent = forms.FloatField()
    words_new = forms.FloatField()
    words_fuzzy50 = forms.FloatField()
    words_fuzzy75 = forms.FloatField()
    words_fuzzy85 = forms.FloatField()
    words_fuzzy95 = forms.FloatField()
    words_match = forms.FloatField()
    words_rep = forms.FloatField()
    words_ice = forms.FloatField()
    #multiply total with this percentage value e.g. 100 * 1.50 (50% rush charge)
    #THIS SHOULD BE A TRUE/FALSE VALUE
    #TODO CHANGE TO TRUE FALSE
    pay_rush = forms.FloatField()

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = ClientJob
        exclude = ("key_field",)

        #fields = ["clientName", "clientContact"]