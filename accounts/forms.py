from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))

    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     # check username
    #     return username


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))