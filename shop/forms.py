from django import forms
from .models import AddCart


class AddCartForm(forms.Form):
    selected_color = forms.CharField(error_messages={'required': 'لطفا از رنگ های بالا رنگ مورد نظر رو انتخاب کنید'})
    selected_size = forms.CharField(error_messages={'required': 'لطفا از سایز های بالا سایز مورد نظر رو انتخاب کنید'})
    selected_quantity = forms.CharField()
    total_price = forms.CharField()


class EditItemCartForm(forms.Form):
    edit_quantity = forms.CharField(required=False)
    edit_size = forms.CharField(required=False)
