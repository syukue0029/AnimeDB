from django import forms
from .models import Item

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('title','place','type','media','year','epsode_number','media_number','production','voiceactor','director','memo')
        widgets = {
                    'title': forms.TextInput(attrs={'placeholder':'例：Fate/stay night'}),
                    'place': forms.TextInput(attrs={'placeholder':'例：テレビ左の棚'}),
                    'type': forms.RadioSelect(),
                    'media': forms.RadioSelect(),
                    'year': forms.NumberInput(attrs={'min':1963}),
                    'epsode_number': forms.NumberInput(attrs={'min':1}),
                    'media_number': forms.NumberInput(attrs={'min':1}),
                    'production': forms.TextInput(attrs={'placeholder':'例：スタジオディーン'}),
                    'voiceactor': forms.TextInput(attrs={'placeholder':'例：杉山紀彰 川澄綾子'}),
                    'director': forms.TextInput(attrs={'placeholder':'例:山口祐司'}),
                    'memo': forms.Textarea(attrs={'rows':4}),
                  }
