from django import forms
from .models import Devtool

class DevtoolForm(forms.ModelForm):
    class Meta:
        model = Devtool
        fields = ('__all__') # 모든 필드를 사용하겠다.