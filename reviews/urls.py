from django.urls import path
from .views import LeaveReviewView, ViewReviews, UpdateReview, DeleteReview

urlpatterns = [
    
    path('', ViewReviews.as_view(), name='reviews'),
    path('leave_review', LeaveReviewView.as_view(), name='leave_review'),
    path('review/<int:pk>/update', UpdateReview.as_view(), name='update_review'),
    path('review/<int:pk>/delete', DeleteReview.as_view(), name='delete_review'),
    
]