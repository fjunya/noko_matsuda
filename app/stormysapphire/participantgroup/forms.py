from django import forms

from participant.models import Participant, ParticipantGroup


class EditForm(forms.Form):
    group_name = forms.CharField(
       max_length=16, required=True,
       widget=forms.TextInput(attrs={'size': 16}))
    info = forms.CharField(
       max_length=64, required=False,
       widget=forms.TextInput(attrs={'size': 64}))

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['participant'] = forms.TypedMultipleChoiceField(
            choices=tuple((x['id'], x['display_name']) for x
                           in Participant.objects.values()),
            required=False)


class DeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['participant_group_id'] = forms.TypedMultipleChoiceField(
            choices=tuple((x['id'], x['group_name']) for x in
                          ParticipantGroup.objects.values('id', 'group_name')),
            required=True)


class ImportForm(forms.Form):
    file = forms.FileField()


class ImportRowForm(EditForm):
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['participant'] = forms.TypedMultipleChoiceField(
            choices=tuple((x['display_name'], x['display_name']) for x
                           in Participant.objects.values()),
            required=False)
