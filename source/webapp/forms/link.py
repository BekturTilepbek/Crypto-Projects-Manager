from django import forms

from webapp.models import Link


class LinkForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            v.field.widget.attrs["class"] = "form-control"
            v.field.widget.attrs["autocomplete"] = "off"

    class Meta:
        model = Link
        fields = ("type", "url")
