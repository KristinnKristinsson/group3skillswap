from django.shortcuts import render, redirect

from .forms import ContactForm


SUBMISSIONS = []

def contact_index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            return render(request, 'contactapp/thankyou.html', {
                'name': message.name,
                'email': message.email,
                'message': message.message,
            })
    else:
        form = ContactForm()
    return render(request, 'contactapp/contact_index.html', {'form': form})



def thankyou_page(request):
    return render(request, 'contactapp/thankyou_page.html', {'submissions': SUBMISSIONS})
