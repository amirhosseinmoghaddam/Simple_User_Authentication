from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterNew(UserCreationForm):
    email = forms.EmailField(required=True)
    age = forms.IntegerField()
    country = forms.CharField(max_length=256)

    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'country', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None