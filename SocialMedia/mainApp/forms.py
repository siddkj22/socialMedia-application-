from django import forms 
from .models import HashTag

class Tweetform(forms.ModelForm):
    class Meta:
        model = HashTag
        fields = ['text']
        labels = {'text': 'tweet:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}



