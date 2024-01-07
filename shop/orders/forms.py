from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'address',
            # 'postal_code',
            'city'
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Имя',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Фамилия',
                }
            ),

            'phone': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Телефон',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Email',
                }
            ),

            'address': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                    "placeholder": 'Дом, улица',
                }
            ),

            'city': forms.Select(
                attrs={
                    "class": "form-select",
                    "style": "border-left: 0; border-top: 0; border-right: 0; padding-left: 0; border-radius: 0",
                },
            )
        }


class OrderUpdateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'paid'
        ]