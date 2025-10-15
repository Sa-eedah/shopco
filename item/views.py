from django.contrib.auth.decorators import login_required  
from django.db.models import Q 
from django.shortcuts import render,get_object_or_404, redirect 

# Import custom forms and models from this app
from .forms import NewItemForm, EditItemForm
from  .models import Category, Item
from shopco.forms import ReviewForm
from shopco.models import Review

"""To restrict access to logged-in users 
   To perform complex queries (OR, AND)
   Rendering templates, retrieving
"""

# Create your views here.
# -------------------------------
# View to list all items (with optional filtering & search)
# -------------------------------
def items(request):
    query = request.GET.get('query')
    category_id = request.GET.get('category')

    all_items = Item.objects.filter(sold=False)

    if category_id:
        all_items = all_items.filter(category_id=category_id)

    if query:
        all_items = all_items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    new_arrivals = all_items.order_by('-created_at')[:8]
    top_selling = all_items.order_by('-rating')[:8]
    categories = Category.objects.all()

    context = {
        'items': all_items,
        'new_arrivals': new_arrivals,
        'top_selling': top_selling,
        'categories': categories,
    }
    return render(request, 'item/items.html', context)


# -------------------------------
# View to display details of a single item
# -------------------------------
def detail(request,pk):
    # Get the item or return 404 if not found
    item = get_object_or_404(Item, pk=pk)
    # Fetch up to 3 related items from the same category, excluding the current one
    related_items = Item.objects.filter(category=item.category, sold=False).exclude(pk=pk)[0:3]
    # Render item detail page
    return render(request, 'item/detail.html', { 
        'item': item, 
        'related_items': related_items
    })



# -------------------------------
# View to create a new item (restricted to logged-in users)
# -------------------------------

@login_required
def new(request):
    if request.method == "POST":
        # Bind form with POST data and uploaded files
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # Save the form but don’t commit yet (we need to set created_by)
            item = form.save(commit=False)
            item.created_by = request.user # Assign logged-in user
            item.save()

            return redirect('item:detail', pk=item.id) # Redirect to the detail page of the new item
    else:
# If GET request → show empty form
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': ' New item', # (❗️probably should say "New item")
    })

# -------------------------------
# View to edit an existing item (restricted to the creator only)
# -------------------------------

@login_required
def edit(request, pk):
    # Ensure the item exists and belongs to the current user
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        # Pre-fill form with existing item data (instance=item)
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()  # Save updates

            return redirect('item:detail', pk=item.id)
    else:

        form = EditItemForm(instance=item) # If GET request → show form with item’s current values

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',# (❗️probably should say "Edit item")

    })

# -------------------------------
# View to delete an item (restricted to the creator only)
# -------------------------------

@login_required
def delete(request, pk):
     # Only allow the owner of the item to delete it
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
# Redirect back to the user’s dashboard after deletion
    return redirect('dashboard:index')

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    reviews = item.reviews.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.item = item
            if request.user.is_authenticated:
                review.user = request.user
            review.save()
            return redirect('item:detail', pk=item.pk)

    context = {
        'item': item,
        'reviews': reviews,
        'form': form
    }
    return render(request, 'item/detail.html', context)
