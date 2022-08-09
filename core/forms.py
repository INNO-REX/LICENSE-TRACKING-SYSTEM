from django import forms
from core.models import License

class LicenseForm (forms.ModelForm):
    class meta:
        model = license
        fields = ('category', 'import', 'date', 'description')
        widget = {
            'date': forms.DateInput (format='%dM%Y',attrs={'class':'form-control','type':'date'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'import': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.RadioSelect(),
            }
        labels = {
                'date': '',
                'description': '',
                'import': '',
                'category': '',


            }
