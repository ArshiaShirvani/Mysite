from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    FormView
)
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(TemplateView):
    template_name = "website/index.html"
    
class AboutView(TemplateView):
    template_name = "website/about.html"
    
    
class ContactView(FormView):
    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("website:contact")
    
    def form_valid(self, form):
        form.save()
        messages.success(
            self.request,"تیکت شما با موفقیت ارسال شد در اسرع وقت پیگیری خواهیم کرد")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(
            self.request,"تیکت شما ارسال نشد لطفا دوباره تلاش کنید"
        )
        return super().form_invalid(form)
