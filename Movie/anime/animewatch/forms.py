from django import forms
from.models import anime

class AnimeForm(forms.ModelForm):
    class Meta:
        model=anime
        fields=['name','desc','year','img']