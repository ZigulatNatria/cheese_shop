from django.forms import ModelForm, forms
from captcha.fields import CaptchaField
from .models import Product, Comment
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        # fields = ('name', 'text', 'price', 'amount', 'image', 'productCategory')
        fields = '__all__'


# class UserCommentForm(ModelForm):
#
#     class Meta:
#         model = Comment
#         exclude = ('is_active')
#         widgets = {'bb': HiddenInput}
#
#
# class GuestCommentForm(ModelForm):
#     captcha = CaptchaField(label='Введите текст с картинки', error_messages={'invalid': 'Неправильный текст'})
#
#     class Meta:
#         model = Comment
#         exclude = ('is_active')
#         widgets = {'bb': forms.HiddenInput}


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    telephone = forms.CharField(max_length=50, label='Телефон') #вписать именно на цифры
    # telephone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000, label='Опишите ваш заказ')