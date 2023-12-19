from django import forms
from .models import RequestMech

# Create your forms here 
class RequestMechForm(forms.ModelForm):
    class Meta:
        model = RequestMech
        fields = '__all__'

        