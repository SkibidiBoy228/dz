from django import forms
from datetime import date, datetime, time, timedelta


class DeliveryForm(forms.Form):
    first_name = forms.CharField(label="Імʼя", max_length=50)
    last_name = forms.CharField(label="Прізвище", max_length=50)
    country = forms.CharField(label="Країна", max_length=50)
    city = forms.CharField(label="Місто", max_length=50)
    region = forms.CharField(label="Область", max_length=50)
    street = forms.CharField(label="Вулиця", max_length=100)
    postal_code = forms.CharField(label="Поштовий індекс", max_length=10)
    delivery_date = forms.DateField(label="Дата доставки")
    delivery_time = forms.TimeField(label="Час доставки")

    def clean_delivery_date(self):
        d = self.cleaned_data['delivery_date']
        if d < date.today() + timedelta(days=1):
            raise forms.ValidationError("Дата доставки має бути не раніше ніж завтра!")
        return d

    def clean_delivery_time(self):
        t = self.cleaned_data['delivery_time']
        work_start = time(9, 0)
        work_end = time(18, 0)

        if not (work_start <= t <= work_end):
            raise forms.ValidationError("Доставка можлива лише з 09:00 до 18:00.")
        return t

    def clean_postal_code(self):
        code = self.cleaned_data['postal_code']
        if not code.isdigit():
            raise forms.ValidationError("Поштовий індекс повинен містити лише цифри.")
        return code

    def clean(self):
        cleaned = super().clean()
        for field in ["first_name", "last_name", "country", "city", "region", "street"]:
            if field in cleaned:
                value = cleaned[field]
                if not value[0].isupper():
                    self.add_error(field, "Повинно починатися з великої літери!")

        return cleaned
