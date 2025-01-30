from django import forms
from django.contrib.auth.forms import UserCreationForm
from manager.models import Worker


class WorkerCreationForm(UserCreationForm):
    position = forms.ModelChoiceField(queryset=Worker.position.field.related_model.objects.all(), required=False)
    email = forms.EmailField(required=True)
    is_superuser = forms.BooleanField(required=False, label="Create as Superuser")

    class Meta:
        model = Worker
        fields = ["username", "position", "email", "password1", "password2", "first_name", "last_name", "is_superuser"]

    def save(self, commit=True):
        worker = super().save(commit=False)
        worker.email = self.cleaned_data["email"]
        worker.position = self.cleaned_data["position"]

        if self.cleaned_data.get("is_superuser"):
            worker.is_superuser = True
            worker.is_staff = True

        if commit:
            worker.save()
        return worker


class WorkerUpdateForm(forms.ModelForm):
    position = forms.ModelChoiceField(queryset=Worker.position.field.related_model.objects.all(), required=False)
    email = forms.EmailField(required=True)
    is_superuser = forms.BooleanField(required=False, label="Superuser Status", initial=False)

    class Meta:
        model = Worker
        fields = ["username", "position", "email", "first_name", "last_name", "is_superuser"]
