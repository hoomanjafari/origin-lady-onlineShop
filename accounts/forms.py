from django import forms
from django.core.exceptions import ValidationError
from .models import MyUser, UserAddress


class RegisterForm(forms.Form):
    mobile = forms.CharField(max_length=13, label='')


class VerifyFrom(forms.Form):
    otp_1 = forms.CharField(max_length=1, label='')
    otp_2 = forms.CharField(max_length=1, label='')
    otp_3 = forms.CharField(max_length=1, label='')
    otp_4 = forms.CharField(max_length=1, label='')


class SetPasswordForm(forms.Form):
    password = forms.CharField(max_length=16)
    confirm_password = forms.CharField(max_length=16)

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_password')

        if p1 and p2 and p1 != p2:
            raise ValidationError('رمز عبور و تکرار رمز عبور باید یکسان باشند !')


class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=13)
    password = forms.CharField(max_length=16)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('fullname', 'email')
        labels = {
            'fullname': '',
            'email': ''
        }


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ('name', 'family', 'address_mobile', 'state', 'city', 'address', 'postal_code')
        labels = {
            '__all__': '',
        }


class ForgotPasswordForm(forms.Form):
    forgot_mobile = forms.CharField(max_length=13, label='')
