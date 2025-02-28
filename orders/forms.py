import re
from django import forms


class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_deliviry = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ],
    )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", "False"),
            ("1", "True"),
        ],
    )

    def clean_phone_number(self):
        data = self.cleaned_data["phone_number"]

        if not data.isdigit():
            raise forms.ValidationError("Телефон должен состоять только из цифр")
        
        pattern= re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data


    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #         ],
    #         initial=0,
    #     )
    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "form-control",
    #             "id": "delivery_address",
    #             "rows": "2",
    #             "placeholder": "Введите адрес доставки",
    #         }
    #     ),
    #     required=False,
    # )
    # payment_on_get = forms.ChoiceField(
    #     choices=[
    #         ("0", 'False'),
    #         ("1", 'True'),
    #         ],
    #     )
