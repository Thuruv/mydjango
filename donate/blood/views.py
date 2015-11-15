from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import *
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, Template, RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from django.core.mail import EmailMessage

import time

from .models import Details
from .forms import AddmeForm,FeedbackForm

def index(request):
    template = 'index.html'
    c = ''
    Context = ''
    return render(request, template, Context)

def contact(request):
    template = 'contact.html'
    Context = {}
    return render(request, template, Context)

def add(request):
    form = AddmeForm(request.POST)
    if form.is_valid():
        s = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('')
    else:
        form = AddmeForm()
    context = {
        "form": form,
    }
    template = "add.html"
    return render(request, template, context)

def thanks(request):
    return render(request, 'thanks.html', {})

def feedback(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        s = form.save(commit=False)
        form.save()
        contact_email =  form.cleaned_data['email']
        form_content = form.cleaned_data['message']
        template = get_template('contact_template.txt')
        context = Context({
                    'contact_email': contact_email,
                    'form_content': form_content,
                })
        content = template.render(context)

        email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" +'<hi@weddinglovely.com>',
            ['zexphyr@outlook.com'],
            headers = {'Reply-To': contact_email }
        )
        email.send()
        return redirect('thanks')
    else:
        form = FeedbackForm()
    context = {
        "form": form,
    }
    return render(request, 'feedback.html', context)
