from django.shortcuts import render
from .models import Project

def projects(request):
    categories = Project.PROJECT_TYPES
    selected_category = request.GET.get('category', 'all')  # fixed key name

    if selected_category == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category=selected_category)

    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'project.html', context)
