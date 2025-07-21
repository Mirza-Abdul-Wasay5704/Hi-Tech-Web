from django.shortcuts import render, get_object_or_404

from .models import Project
from core.views import get_company_info


def project_list(request):
    projects = Project.objects.all().order_by("-completion_date")
    context = {
        "company_info": get_company_info(),
        "projects": projects,
    }
    return render(request, "projects/project_list.html", context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.exclude(pk=pk).order_by("?")[:3]
    context = {
        "company_info": get_company_info(),
        "project": project,
        "related_projects": related_projects,
    }
    return render(request, "projects/project_detail.html", context)
