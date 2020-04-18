from django import forms
from .models import Translate

class TranslateForm(forms.ModelForm):

    class Meta:
        model = Translate
        #fields = ['lang_1', 'lang_2', 'text']
        exclude = ['user', 'translation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['lang_1'].widget.attrs.update({
                'class': 'btn btn-secondary dropdown-toggle'
            })

        self.fields['text'].widget.attrs.update({
                'class': 'form-control mt-2', 'placeholder': 'Insert text',  'rows': '3'
            })

        self.fields['lang_2'].widget.attrs.update({
                'class': 'btn btn-secondary dropdown-toggle'
            })