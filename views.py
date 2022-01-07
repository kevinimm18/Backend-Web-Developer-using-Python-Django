from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from .forms import ContactForm
from .models import contact, Content_List

from django.views.generic import ListView, DetailView

# Create your views here.

def base(request):
    return render(request, 'base.html', {})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()

    context = {
        'form' : form
    }
    return render(request, 'contact.html', context)

def project(request):
    return render(request, 'project.html', {})

def services(request):
    return render(request, 'services.html', {})

# def content_list(request):
#     return render(request, 'content_list.html', {})

class Content_ListListView(ListView):
    model = Content_List
    template_name = "content_list.html"
    context_object_name = 'content_list'
    ordering = ['-Published']
    paginate_by = 3

class Content_ListDetailView(DetailView):
    model = Content_List
    template_name = "content_detail.html"
    context_object_name = 'detail'



# class traveling(TemplateView):
#     template_name = "traveling.html"

# class about(TemplateView):
#     template_name = "about.html"

# class contact(ListView):
#     model = contact
#     template_name = "contact.html"

#     def form_valid(self, POST):
#         form = ContactForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             form = ContactForm()

#         context = {
#             'form' : form
#         }
#         return render(request, 'contact.html', context)



#     form = ContactForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ContactForm()

#     context = {
#         'form' : form
#     }
#     template_name = "contact.html"

# class project(TemplateView):
#     template_name = "project.html"

# class services(TemplateView):
#     template_name = "services.html"

