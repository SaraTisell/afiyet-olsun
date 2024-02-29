from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from .models import Review
from .forms import ReviewForm, ApproveReviewsForm



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


class UpdateReview(SuccessMessageMixin, UpdateView):
    """
    Function to update an exisiting review
    Render ApproveReviewForm for staff
    and ReviewForm for user
    """
    model = Review 
    template_name = 'reviews/update_review.html'
    success_message = "The review was successfully updated!"

    def get_form_class(self):

        if self.request.user.is_staff:
            return ApproveReviewsForm
        else:
            return ReviewForm

    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('manage_reviews')
        else:
            return reverse_lazy('reviews')


class DeleteReview(SuccessMessageMixin, DeleteView):
    """
    Function to delete an existing review
    """
    model = Review
    template_name = 'reviews/delete_review_confirm.html'
    success_url = reverse_lazy('reviews')
    success_message = "The review was successfully deleted!"


class ManageReviewsStaff(TemplateView):

    template_name = 'reviews/manage_reviews.html'


class ManageReviewsView(UserPassesTestMixin, ListView):
    """
    View to render all reviews for staff
    Approved and not approved
    """
    model = Review
    template_name = 'reviews/manage_reviews.html'
    context_object_name = "reviews"

    def get_queryset(self):

        if self.request.user.is_staff:
            return Review.objects.all()

    def test_func(self):
        """ Test user is staff """
        if self.request.user.is_staff:
            return True
