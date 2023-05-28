from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, PlainText, News


class BlogListView(ListView):
    model = Post
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_me_records'] = PlainText.objects.all()
        context['seether_news'] = News.objects.order_by('-created')[0:3]
        return context


class AllNewsView(ListView):
    model = News
    template_name = "all_news.html"
    ordering = ["-created"]


class BlogDetailView(DetailView):
    model = News
    template_name = "post_detail.html"
