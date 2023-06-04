from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, PlainText, News, Subscribers
from django.views.generic.edit import CreateView
from .forms import SubscribersForm, MailMessageForm
from django.core.mail import send_mail


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


# class EmailSubscription(CreateView):
# model = Subscribers
# template_name = "join-maling-list.html"
# fields = ["email", ]

def mailing(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('join-mailing-list')
    else:
        form = SubscribersForm()
    context = {
        'form': form,
    }
    return render(request, 'join-mailing-list.html', context)


