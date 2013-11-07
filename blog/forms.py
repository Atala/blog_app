# Create your forms here.
# -*- coding: utf-8 -*-

from django import forms 

from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    name = forms.CharField(label = 'Nom',  widget = forms.TextInput)
    subject = forms.CharField(max_length=100, label = 'Objet du message', widget = forms.TextInput)
    message = forms.CharField(label = 'Message',  widget = forms.Textarea)
    sender = forms.EmailField(label = 'Votre adresse', widget = forms.EmailInput)
    cc_myself = forms.BooleanField(required=False, label = 'Recevoir une copie du mail')
    
    def clean(self):
	if self.cleaned_data is None:
	    raise ValidationError("Message vide!")
	if not self.has_changed():
	    raise ValidationError("Hey! Ecris quelque chose!")
	return self.cleaned_data
