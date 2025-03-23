from django import forms

from webapp.models import Project


class ProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            v.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Project
        fields = ("name", "description", "status", "priority", "info")
