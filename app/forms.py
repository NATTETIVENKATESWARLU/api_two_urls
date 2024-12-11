from django import forms
from app.models import *

class employee_data(forms.ModelForm):
    def clean_esal(self):
        data=self.cleaned_data["esal"]
        if data<5000:
            raise forms.ValidationError("provide data more then 5000")
        return data
    class Meta:
        model=employees
        fields="__all__"