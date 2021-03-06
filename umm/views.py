from django.shortcuts import render

from.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.db.models import Q


class PostListView(LoginRequiredMixin,ListView):
    model=Post
    template_name='umm/blog.html'
    context_object_name='posts'
    ordering=['-age'] 

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =['title', 'content']
    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title', 'content']
    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False



    

def sagol(request):
    return render(request,'umm/sagol.html',{'title':'False'})









