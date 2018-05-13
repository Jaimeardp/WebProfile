from django.shortcuts import render
from .models import Document

# Create your views here.

def portfolio_list_view(request):
    projects = Document.objects.all()
    return render(request, "portfolio.html", {'projects':projects})
