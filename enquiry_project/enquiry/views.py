# enquiry/views.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import InquiryForm

def inquiry(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(
                subject,
                f"From: {name} <{email}>\n\n{message}",
                email,
                ['21uad020@kamarajengg.edu.in'],  # Replace with your email address
                fail_silently=False,
            )
            return redirect('inquiry_success')
    else:
        form = InquiryForm()
    return render(request, 'inquiry_form.html', {'form': form})

def inquiry_success(request):
    return render(request, 'inquiry_success.html')
