from django import forms

from django.core.exceptions import ValidationError

from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )
        

# Разные виды форм(требуется для обучения)


class FullForms(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(
        label='Фамилия', required=False, help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='forms.DateInput'
    )
    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea(attrs={'cols': 90, 'rows': 3}),
        help_text='forms.Textarea'
    )
    mail = forms.EmailField(
        label='Почта',
        help_text='EmailField'
    )
    myself = forms.BooleanField(
        label='Выбор',
        help_text='BooleanField'
    )
