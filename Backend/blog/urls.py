from django.urls import path,re_path
from . import views

app_name = "blog"

urlpatterns = [
    path("post-list/",views.PostListView.as_view(),name="post-list"),
    re_path(r"post/detail/(?P<slug>[-\w]+)/",views.PostDetailView.as_view(),name="post-detail"),
    path('submit-comment/',views.SubmitCommentView.as_view(),name="submit-comment"),
]