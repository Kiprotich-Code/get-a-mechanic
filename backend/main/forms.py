from django import forms
from .models import RequestMech
from accounts.models import CustomUser

# Create your forms here 
class RequestMechForm(forms.ModelForm):
    class Meta:
        model = RequestMech
        fields = ['location', 'car_issue', 'priority', 'expected_time', 'expected_budget',]

        def __init__(self, *args, **kwargs):
            super(RequestMech, self).__init__(*args, **kwargs)

            self.fields['mech'].queryset = CustomUser.objects.filter(user_type='mechanic')
