from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import render
from .models import Review

class LeaveReviewView(CreateView):
    """
    View to render form so
    users can leave reviews
    """
    template_name = 'reviews/all_reviews.html'
    form_class = ReviewForm
    success_url = "/reviews/all_reviews/"

    def form_valid(self, form):

        review.save()
        message = f"Your review have ben submitted and waiting for approval"
        message.success(self.request, message)
        return super().form_valid(form)

class ViewReviews(ListView):
    """
    View to display all exisiting reviews
    """
    model = Review
    template_name = 'reviews/all_reviews.html'

    def get_queryset(self):
        return Review.object.filter(status=1)

class UpdateReview(UpdateView):
    """
    Function to update an exisiting review
    """
    model = Review 
    form_class = ReviewForm
    template_name = 'reviews/all_reviews.html'
    success_url = reverse_lazy('reviews')


class DeleteReview(DeleteView):
    """
    Function to delete an existing review
    """
    model = Review
    template_name = 'reviews/delete_review_confirm.html'
    success_url = reverse_lazy('all_reviews')
    success_message = "The review was successfully deleted!"