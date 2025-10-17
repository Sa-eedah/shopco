from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from item.models import Category, Item
from .forms import SignupForm, ReviewForm
from .models import Review

# ====== Homepage ======
def index(request):
    new_arrivals = Item.objects.all().order_by('-created_at')[:4]
    top_selling = Item.objects.all().order_by('-created_at')[:4]
    categories = Category.objects.all()
    reviews = Review.objects.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:index')

    return render(request, 'shopco/index.html', {
        'new_arrivals': new_arrivals,
        'top_selling': top_selling,
        'categories': categories,
        'reviews': reviews,
        'form': form
    })


# ====== Contact Page ======
def contact(request):
    return render(request, 'shopco/contact.html')


# ====== Signup ======
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect('shopco:login')
    else:
        form = SignupForm()

    return render(request, 'shopco/signup.html', {'form': form})


# ====== Customer Reviews ======
def customer_reviews(request):
    reviews = Review.objects.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shopco:customer_reviews')

    return render(request, 'shopco/reviews.html', {'reviews': reviews, 'form': form})


# ====== Custom Logout with message ======
class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, "You’ve been logged out successfully.")
        return response
