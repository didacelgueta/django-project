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


'''
    text = forms.CharField(max_length=400,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2', 'placeholder': 'Insert text',  'rows': '7'}))
'''

'''
class TranslateForm(forms.Form):
    lang_1 = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select(
            choices=LANGUAGES,
            attrs={'class': 'btn btn-secondary dropdown-toggle'})
    )
    text = forms.CharField(max_length=400,
        widget=forms.TextInput(
            attrs={'class': 'form-control mt-2', 'placeholder': 'Insert text',  'rows': '7'}))
    lang_2 = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=LANGUAGES,
    )
    translated_text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Translate
        fields = ['lang_1', 'lang_2', 'text', 'translated_text']




    lang = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=LANGUAGES,
    )
    text = forms.CharField(widget=forms.Textarea(attr='class': 'form-control mt-2', 'placeholder': 'Insert text',  'rows': '7'))



class ToLangForm(forms.Form):
    lang = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=LANGUAGES,
    )
    text = forms.CharField(widget=forms.Textarea)



lang_1 = forms.MultipleChoiceField(
    required=True,
    widget=forms.CheckboxSelectMultiple,
    choices=LANGUAGES,
)
text_1 = forms.CharField(widget=forms.Textarea)
class Meta:
    model = Translate
    fields = ['text_1']
    widgets = {
        'text': forms.CheckboxSelectMultiple(
        attrs={'class': 'dropdown-menu btn btn-dark dropdown-toggle float-right', 'type': 'button', 'data-toggle': 'dropdown'}
        )
    }

'''
