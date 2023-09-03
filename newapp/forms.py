from django.forms import ModelForm
from newapp.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        # fields = "__all__"
        fields = ["name", "age", "mobile"]
