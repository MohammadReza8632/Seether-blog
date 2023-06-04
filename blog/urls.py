from django.urls import path
from .views import BlogListView, BlogDetailView, AllNewsView
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("news-seether", AllNewsView.as_view(), name="all_news"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    # path("join-maling-list", TemplateView.as_view(template_name="join-maling-list.html"), name="join-maling-list"),
    # path("join-maling-list", EmailSubscription.as_view(), name="join-maling-list"),
    path("join-mailing-list", views.mailing, name="join-mailing-list"),


]
