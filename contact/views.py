from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Contact, Quote
from .forms import ContactForm, QuoteForm
from core.views import get_company_info

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send email notification
            subject = f'New Contact Message from {contact.name}'
            message = f"""
                Name: {contact.name}
                Email: {contact.email}
                Phone: {contact.phone}
                Message: {contact.message}
            """
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception as e:
                messages.error(request, 'There was an error sending your message. Please try again later.')
                return redirect('contact:contact')
            
            return redirect('contact:success')
    else:
        form = ContactForm()
    
    context = {
        'company_info': get_company_info(),
        'form': form,
    }
    return render(request, 'contact/contact.html', context)

def request_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save()
            
            # Send email notification
            subject = f'New Quote Request from {quote.name}'
            message = f"""
                Name: {quote.name}
                Email: {quote.email}
                Phone: {quote.phone}
                Service Type: {quote.service_type}
                Details: {quote.details}
            """
            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception as e:
                messages.error(request, 'There was an error sending your quote request. Please try again later.')
                return redirect('contact:quote')
            
            return redirect('contact:success')
    else:
        initial_service = request.GET.get('service', '')
        form = QuoteForm(initial={'service_type': initial_service})
    
    context = {
        'company_info': get_company_info(),
        'form': form,
    }
    return render(request, 'contact/quote.html', context)

def success(request):
    context = {
        'company_info': get_company_info(),
    }
    return render(request, 'contact/success.html', context)
