from django.shortcuts import render
from .models import Skill

def myskills(request):
    # Get all distinct categories from skills
    categories = Skill.SKILLS_CATEGORY
    selected_category = request.GET.get('category', 'all')
    
    if selected_category == 'all':
        skills = Skill.objects.all().order_by('order')
    else:
        skills = Skill.objects.filter(category=selected_category)
    
    context = {
        'skills': skills,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'skills.html', context)