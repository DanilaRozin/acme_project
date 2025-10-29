from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(
        label='Фамилия', required=False, help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date'}),
    )


class FullForms(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(
        label='Фамилия', required=False, help_text='Необязательное поле'
    )
    birthday = forms.DateField(
        label='Дата рождения',
        # Указываем, что виджет для ввода даты должен быть с типом date.
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text='forms.DateInput'
    )
    comment = forms.CharField(
        label='Комментарий',
        # Указываем, что виджет для ввода даты должен быть с типом date.
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
