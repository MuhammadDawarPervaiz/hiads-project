from django.shortcuts import render

def viewForm(request):
    return render(request, 'surveys/form.html')
