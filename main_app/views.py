from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from main_app.models import Post, Comment, Profile
from main_app.forms import PostForm, CommentForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

class Home(LoginView):
    template_name = 'home.html'

# class PostCreate(LoginRequiredMixin, CreateView):
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    # success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

# class PostUpdate(LoginRequiredMixin, UpdateView):
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

# class PostDelete(LoginRequiredMixin, DeleteView):
class PostDelete(DeleteView):
    pass

# Profile view for signed-in user
@login_required
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)
    user_posts = Post.objects.filter(user=user)
    post_count = user_posts.count()
    context = {
        'profile': profile,
        'user_posts': user_posts,
        'post_count': post_count,
    }
    return render(request, 'profile/profile.html', context)
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_index')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        login(self.request, user)
        return response
    
    def get_success_url(self):
        return '/create/'


class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments/comment_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
