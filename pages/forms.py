from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "phone", "message")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["subject"].widget.attrs["class"] = "form-control"
        self.fields["phone"].widget.attrs["class"] = "form-control"
        self.fields["message"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "your Name"
        self.fields["email"].widget.attrs["placeholder"] = "your Email"
        self.fields["subject"].widget.attrs["placeholder"] = "Newest Philanthropist"
        self.fields["message"].widget.attrs["placeholder"] = "Hi there, I would like to ..."
        self.fields["phone"].widget.attrs["placeholder"] = "+1234567890"

        self.fields["message"].widget.attrs["cols"] = "30"
        self.fields["message"].widget.attrs["row"] = "4"
        self.fields["message"].widget.attrs["id"] = "message"
