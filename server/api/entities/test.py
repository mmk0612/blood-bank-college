from django.db import models
from django import forms

class Test(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('field1', 'field2')

