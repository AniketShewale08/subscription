from django.shortcuts import render
from .models import Product
from .forms import RatingForm

# Create your views here.
def pricing_table(request):
    subscription_plans = Product.objects.all()
    for plan in subscription_plans:
        plan.rating_percentage = (plan.ratings / 5) * 100 if plan.ratings is not None else 0
        plan.remaining_stars = 5 - plan.ratings if plan.ratings is not None else 5
    return render(request, 'price_table.html', {'subscription_plans': subscription_plans})


from django.shortcuts import get_object_or_404, redirect

def rate_subscription(request, plan_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['ratings']
            plan = get_object_or_404(Product, pk=plan_id)
            plan.ratings = rating
            plan.save()
    return redirect('pricing_table') 
