from django.urls import path
from .views import LeaveReviewView, ViewReviews, UpdateReview, DeleteReview

urlpatterns = [
    path('', LeaveReviewView.as_view(), name='reviews'),
    path('all_reviews/', ViewReviews.as_view(), name='all_reviews'),
    path('all_reviews/<int:pk>/update', UpdateReview.as_view(), name='update_review'),
    path('all_reviews/<int:pk>/delete', DeleteReview.as_view(), name='delete_review'),
]