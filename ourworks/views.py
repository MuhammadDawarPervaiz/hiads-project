from django.shortcuts import render, redirect, get_object_or_404
from .models import Work, Category

def home(request):

    works = Work.objects
    categories = Category.objects
    return render(request, 'ourworks/base.html', {'works':works, 'categories':categories})
