from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Column, Row


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ("user",)
        widgets = {"date": forms.widgets.DateInput(attrs={"type": "date"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["date"].widget_attrs(widget=forms.TextInput(attrs={"type": "date"}))
        self.helper.layout = Layout(
            Fieldset(
                "Order Tiket",
                Row(
                    Column(
                        "ticket",
                    ),
                    Column(
                        "qty",
                    ),
                ),
                "date",
            ),
        )
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Tambah Order"))
