from django.shortcuts import render, get_object_or_404
from .models import Service
from core.views import get_company_info

def service_list(request):
    services = Service.objects.all().order_by('order', 'name')
    context = {
        'company_info': get_company_info(),
        'services': services,
    }
    return render(request, 'services/service_list.html', context)

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    related_services = Service.objects.exclude(pk=pk).order_by('?')[:3]
    context = {
        'company_info': get_company_info(),
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)
