from django.shortcuts import render
from myproject.models import Project
from review.models import Review
from .models import UserProfile, FAQ
from myskills.models import Skill

# Create your views here.
def home(request):
    user = UserProfile.objects.first()
    projects = Project.objects.all()
    Skills = Skill.objects.all()
    reviews = Review.objects.filter(is_active=True).order_by('-date')[:3]
    total_projects = Project.objects.count()
    faq = FAQ.objects.all()
    
    context = {
        'featured_projects': projects,
        'reviews': reviews,
        'user': user,
        'skills': Skills,
        'total_projects': total_projects,
        'faqs': faq,
    }
    return render(request, 'index.html', context)