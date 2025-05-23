from django.shortcuts import render
from .models import Certificate

def certificates_view(request):
    # Get all distinct categories
    categories = Certificate.CATEGORY_CHOICES
    
    # Get selected category from URL parameter
    selected_category = request.GET.get('category', 'all')
    
    # Filter certificates based on category
    if selected_category == 'all':
        certificates = Certificate.objects.all().order_by('-issue_date')
    else:
        certificates = Certificate.objects.filter(category=selected_category).order_by('-issue_date')
    
    context = {
        'certificates': certificates,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'certificates.html', context)