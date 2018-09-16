from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Work, Category, Subscribe
from .forms import SubscriberForm, ContactForm

def home(request):

    works = Work.objects
    categories = Category.objects
    message = ""

    if request.method == 'GET':
        subscriberform = SubscriberForm()
        contactform = ContactForm()
        return render(request, 'ourworks/base.html', {'subscriberform':subscriberform, 'contactform':contactform , 'works':works, 'categories':categories})

    if request.method == 'POST':
        subscriberform = SubscriberForm(request.POST)
        if subscriberform.is_valid():
            email = subscriberform.cleaned_data['email']
            subscriberform.save()
            message = 'You have subscribed successfully'
            subscriberform = SubscriberForm()

        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            name = contactform.cleaned_data['name']
            email = contactform.cleaned_data['email']
            message = contactform.cleaned_data['message']


            send_mail(
                'Contact Form',
                name + '\n\n' + message,
                email,
                ['m.dawarpervaiz@gmail.com'],
                fail_silently=False,
            )


            message = 'You Message has been sent successfully'
            contactform = ContactForm()

        return render(request, 'ourworks/base.html', {'subscriberform':subscriberform, 'contactform':contactform, 'works':works, 'categories':categories, 'message':message})
