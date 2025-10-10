from django.shortcuts import render, redirect

from item.models import Category, Item # Import models from the item app

from .forms import SignupForm # Import the custom signup for

# Create your views here.
"""Homepage"""

def index(request):
    new_arrivals = Item.objects.all().order_by('-created_at')[:4]
    top_selling = Item.objects.all().order_by('-created_at')[:4]
    categories = Category.objects.all()

    return render(request, 'shopco/index.html', {
        'new_arrivals': new_arrivals,
        'top_selling': top_selling,
        'categories': categories,
    })

# View for the contact page
def contact(request):
    # Simply render the contact template
    return render(request, 'shopco/contact.html')

# View for the signup page
def signup(request):
    # If the form is submitted with POST request
    if request.method == 'POST':
        # Bind form with POST data
        form = SignupForm(request.POST)
# If the form is valid, save the user to the database
        if form.is_valid():
            form.save()
# Redirect to the login page after successful signup
        return redirect('/login/')
    
    else:
        # If GET request, display an empty signup form
        form = SignupForm
# Render the signup template with the form
    return render(request, 'shopco/signup.html', {
        'form':form
    })
