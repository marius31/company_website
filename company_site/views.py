from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

#from company_website.forms import ContactForm

def index(request, context={}, template='index.html'):
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def about(request, context={}, template='about.html'):    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def projects(request, context={}, template='projects.html'):    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def interior_design(request, context={}, template='interior_design.html'):    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def exterior_design(request, context={}, template='exterior_design.html'):    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def constructions(request, context={}, template='constructions.html'):    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def installations(request, context={}, template='installations.html'):    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def customer_advice(request, context={}, template='customer_advice.html'):    
    return render_to_response(template, context,
                              context_instance=RequestContext(request))

def contact(request, context={}, template='contact.html'):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        subject = 'Contact - amenajariprofi.ro'
        sender = cd['email']
        message = cd['body']
        message += """\n\n** Mesaj generat automat de pe http://amenajariprofi.ro/contact/ din partea %s **""" % sender

        to = 'marius.gheorghe22@yahoo.com'
        send_mail(subject, message, sender, [to], fail_silently=True)

        return HttpResponseRedirect(reverse('contact_done'))
    else:
        form = ContactForm()

    context.update({
        'form': form,
        #'selected_flag': 'contact',
    })

    return render_to_response(template, context,
		              context_instance=RequestContext(request))
