from django.urls import path,re_path
from . import views

app_name = "library"

urlpatterns = [
    path("book-list/",views.BookListView.as_view(),name="book-list"),
    # re_path(r"book/detail/(?P<slug>[-\w]+)/",views.BookDetailView.as_view(),name="book-detail"),
    # path('submit-comment/',views.SubmitCommentView.as_view(),name="submit-comment"),
]