from django import forms


class InformationEditForm(forms.Form):
    body = forms.CharField(
        max_length=1000, required=False, widget=forms.Textarea())
