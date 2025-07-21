from django.shortcuts import render
from .models import CompanyInfo
from services.models import Service
from projects.models import Project
from django.core.cache import cache

def get_company_info():
    """Get or create company info from cache or database."""
    company_info = cache.get('company_info')
    if not company_info:
        company_info = CompanyInfo.objects.first()
        if not company_info:
            company_info = CompanyInfo.objects.create()
        cache.set('company_info', company_info)
    return company_info

def home(request):
    context = {
        'company_info': get_company_info(),
        'services': Service.objects.all()[:4],
        'featured_projects': Project.objects.all().order_by('-completion_date')[:3]
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'company_info': get_company_info(),
    }
    return render(request, 'core/about.html', context)
