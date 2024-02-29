from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for users to leave a review
    """
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


class ApproveReviewsForm(forms.ModelForm):
    """
    Form for staff to approve reviews
    """
    class Meta:
        model = Review
        fields = ['approved',]
        labels = {'approved': 'Approved'}
