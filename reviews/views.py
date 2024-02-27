from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from .models import Review
from .forms import ReviewForm

class LeaveReviewView(CreateView):
    """
    View to render form so
    users can leave reviews
    """
    model = Review
    template_name = 'reviews/leave_review.html'
    form_class = ReviewForm
    success_url = reverse_lazy('reviews')

    def form_valid(self, form):

        review = form.save(commit=False)
        review.author = self.request.user

        review.save()
        message = f"Your review have been submitted and waiting for approval"
        messages.success(self.request, message)
        return super().form_valid(form)


class ViewReviews(ListView):
    """
    View to display all existing reviews
    """
    model = Review
    template_name = 'reviews/reviews.html'


    def get_queryset(self):
        return Review.objects.filter(approved=True)

class UpdateReview(UpdateView):
    """
    Function to update an exisiting review
    """
    model = Review 
    form_class = ReviewForm
    template_name = 'reviews/update_review.html'
    success_url = reverse_lazy('reviews')
    success_message = "Your review was successfully updated!"


class DeleteReview(DeleteView):
    """
    Function to delete an existing review
    """
    model = Review
    template_name = 'reviews/delete_review_confirm.html'
    success_url = reverse_lazy('reviews')
    success_message = "The review was successfully deleted!"