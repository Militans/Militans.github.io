from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from .utils import predict_stars

def review_predict(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.predicted_stars = predict_stars(review.text)  # Предсказание звёзд
            review.save()
            return redirect('review_result', pk=review.pk)
    else:
        form = ReviewForm()
    return render(request, 'review_form.html', {'form': form})

def review_result(request, pk):
    review = Review.objects.get(pk=pk)
    return render(request, 'review_result.html', {'review': review})
