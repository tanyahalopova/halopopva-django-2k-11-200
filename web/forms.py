from django import forms
from django.contrib.auth import get_user_model
from django.forms import NullBooleanField

from web.models import Inventory, KindOfSport

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error("password", "Пароли не совпадают")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", "username", "password")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class InventoryForm(forms.ModelForm):
    def save(self, commit=True):
        form = super().save(commit)
        form.user.add(self.initial.get('user'))
        return form
    class Meta:
        model = Inventory
        fields = ('title', 'kindOfSport', 'rating')


class KindOfSportForm(forms.ModelForm):
    def save(self, commit=True):
        form = super().save(commit)
        form.user.add(self.initial.get('user'))
        return form

    class Meta:
        model = KindOfSport
        fields = ('title', 'description')

class InventoryFilterForm(forms.Form):
    search = forms.CharField(
        label="Название:",
        widget=forms.TextInput(attrs={"placeholder": "Поиск"}),
        required=False
    )
