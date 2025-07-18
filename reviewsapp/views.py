from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review
from skills.models import AddSkills
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def add_review(request, username, skill_id, skill_name):
    reviewee = get_object_or_404(User, username=username)
    skill = get_object_or_404(AddSkills, pk=skill_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewee = reviewee
            review.skill = skill
            review.save()
            return redirect('reviewsapp:review_list')  
    else:
        form = ReviewForm()

    context = {
        "form": form,
        "reviewee": reviewee,
        "skill": skill,
    }
    return render(request, 'reviewsapp/add_review.html', context)

@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviewsapp/review_list.html', {'reviews': reviews})
