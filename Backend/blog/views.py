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
from .models import PostModel,PostCategory,PostStatusType,CommentModel
from django.core.exceptions import FieldError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import SubmitCommentForm
from django.urls import reverse,reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class PostListView(ListView):
    template_name = "blog/post-list.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = PostModel.objects.filter(
            status=PostStatusType.active.value)
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if query:
            queryset = queryset.filter(title__icontains=query) 
        if category:
            queryset = queryset.filter(category__name__iexact=category)
    
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = PostCategory.objects.all()
        return context
    
class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    queryset = PostModel.objects.filter(status=PostStatusType.active.value)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = CommentModel.objects.filter(post=post.id)
        context["total_comments"] = CommentModel.objects.filter(post=post.id).count()
        return context
    
    
class SubmitCommentView(LoginRequiredMixin,FormView):
    
    http_method_names = ["post"]
    model = CommentModel
    form_class = SubmitCommentForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success (
            self.request,"دیدگاه شما با موفقیت ثبت گردید "
        )
        form.save()
        post = get_object_or_404(PostModel, id=self.request.POST.get('post'))
        return HttpResponseRedirect(reverse_lazy('blog:post-detail', kwargs={'slug': post.slug}))
    
    def form_invalid(self, form):
        messages.error(
            self.request,"دیدگاه شما ثبت نشد دوباره تلاش کنید"
        )
        return super().form_invalid(form)
    
    def get_success_url(self):
        return redirect(reverse_lazy("blog:post-list"))