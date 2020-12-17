from django.http import request
from django.http.response import  HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Profile
from .forms import PostForm

def home(request):
    return render(request, 'home.html', {})

class QueriesView(ListView):
    model = Post
    template_name = 'queries.html'
    ordering = ['-post_date']
   

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_query.html'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_query.html'
    fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_query.html'
    success_url = reverse_lazy('home')