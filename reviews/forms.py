from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'rating',
            'content',
        ]

        labels = {
            'content': 'Comment'
        }

        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Add Your Comments Here', 'class': 'forms-input'}),
        }