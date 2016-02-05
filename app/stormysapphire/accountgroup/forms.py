from django import forms
from account.models import AccountGroup


class EditForm(forms.Form):
    name = forms.CharField(
       max_length=16, required=True,
       widget=forms.TextInput(attrs={'size': 16}))
    info = forms.CharField(
       max_length=64, required=False,
       widget=forms.TextInput(attrs={'size': 64}))


class DeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['account_group_id'] = forms.TypedMultipleChoiceField(
            choices=tuple((x['id'], x['name']) for x in
                          AccountGroup.objects.values('id', 'name')),
            required=True)


class ImportForm(forms.Form):
    file = forms.FileField()


class ImportRowForm(EditForm):
    pass
