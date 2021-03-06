from django import forms
from django.forms import ModelForm, Textarea
from .models import *

class ResponseForm(ModelForm):
    class Meta:
        model = IntraResponse
        fields = ('company','profile','rounds','questions','review','offer','rating')
        widgets = {
            'questions': Textarea(attrs={'rows': 5}),
            'review': Textarea(attrs={'rows': 3}),
        }

    def save(self, user_id, commit=True):
        form = super(ResponseForm, self).save(commit=False)
        form.name = User.objects.get(pk=user_id)
        if commit:
            form.save()
            return form

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude=()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
        widgets = {
            'body': Textarea(attrs={'rows': 3}),
        }
