from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def all_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'all_contacts.html', {'contacts': contacts})