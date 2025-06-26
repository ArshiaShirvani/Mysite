from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    FormView
)
from .models import BookModel,BookCategory,BookStatusType,BookCommentModel
from django.core.exceptions import FieldError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

class BookListView(TemplateView):
    template_name = "library/library-list.html"
    
    

    
    
