from django.shortcuts import render, redirect
from JeraldTest3.forms import ContactForm

def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/contact.html", context)

