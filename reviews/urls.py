from django.urls import path
from .views import review_predict, review_result

urlpatterns = [
    path('predict/', review_predict, name='review_predict'),
    path('result/<int:pk>/', review_result, name='review_result'),
]