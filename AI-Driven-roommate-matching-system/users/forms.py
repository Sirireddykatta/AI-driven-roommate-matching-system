from django import forms

from django.contrib.auth.hashers import make_password

from .models import User
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields =  ['location','profile_picture','password','first_name','last_name','username']
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','autocomplete': 'off'}),
            'location': forms.TextInput(attrs={'class': 'form-control','autocomplete': 'off'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }
    # If the field has errors, add a 'is-invalid' class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Apply 'form-control' class and placeholder to all fields
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {field.label}',
                'autocoomplete':'off'
            })
            
            # Ensure the password field is rendered as a password input
            if field_name in ['password']:
                field.widget = forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder': f'Enter {field.label}',
                     'autocoomplete':'off'
                })
                
            # If the field has errors, add a 'is-invalid' class
            if self.errors.get(field_name):
                field.widget.attrs.update({
                    'class': field.widget.attrs.get('class', '') + ' is-invalid',
                })
        
    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
