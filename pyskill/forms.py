from django import forms
from pyskill.models import Dispatch


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'




class DispatchForm(StyleMixin, forms.ModelForm):
    class Meta:
        model = Dispatch
        fields = ('mail_to_send',)


