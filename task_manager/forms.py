from django import forms

from task_manager.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Task content"
            }
        )
    )
    deadline = forms.DateTimeField(
        widget=forms.SelectDateWidget,
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
