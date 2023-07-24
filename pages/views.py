from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from .forms import ContactForm
from .models import *
from django.views.generic import DetailView


class HomeView(View):
    form_class = ContactForm
    template_name = "home.html"
    success_url = ""
    success_message = "We have received your message and we will get back to you soon"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        readournews = ReadOurNew.objects.all()
        testimonies = Testimony.objects.all()
        philanthropists = Philanthropist.objects.all()

        context = {
            "form": form,
            "readournews": readournews,
            "testimonies": testimonies,
            "philanthropists": philanthropists,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST)
            context = {"form": form}
            if form.is_valid():
                form.save()

                messages.success(request, self.success_message)
                return redirect(self.success_url)
            else:
                print("Error in creating form", form.errors)
               
               

        except Exception as e:
            print("Error", e)
            return render(request, self.template_name, context)


class PhilanthropistDetailView(DetailView):
    model = Philanthropist
    template_name = 'philanthropist_detail.html'
    context_object_name = "philanthropist"


class HomeContactView(View):
    form_class = ContactForm
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST)
            context = {"form": form}
            if form.is_valid():
                form.save()                
                messages.success(request, "We received your contact and we will get back to you soon")
                return redirect('home')
            else:
                print("Error in creating contact", form.errors)
                
        except Exception as e:
            print("Error", e)
        return render(request,self.template_name, context)


class ContactView(View):
    form_class = ContactForm
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        try:
            form = self.form_class(request.POST)
            context = {"form": form}
            if form.is_valid():
                form.save()                
                messages.success(request, "We received your contact and we will get back to you soon")
                return redirect('home')
            else:
                print("Error in creating contact", form.errors)
                
        except Exception as e:
            print("Error", e)
        return render(request,self.template_name, context)
