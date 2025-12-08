from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse, reverse_lazy

from .models import Post, Comment
from .forms import (
    CustomUserCreationForm,
    ProfileForm,
    PostForm,
    CommentForm
)

from .models import Post, Comment
from .forms import CommentForm
from django.db.models import Q

class SearchResultsView(ListView):
    model = Post
    template_name = "blog/search_results.html"
    context_object_name = "posts"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if not query:
            return Post.objects.none()

        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

def register_view(request):
    if request.user.is_authenticated:
        return redirect('blog:profile')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created. You can now log in.')
            return redirect('blog:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'blog/profile.html', {'profile': profile})

@login_required
def profile_edit_view(request):
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        u_email = request.POST.get('email')
        # Update user email safely via form-like check
        if u_email:
            user.email = u_email
            user.save()
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('blog:profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'blog/profile_edit.html', {'form': form, 'user': user})


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # blog/templates/blog/post_list.html
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # blog/templates/blog/post_detail.html
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'    # used for create & update

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    def get_initial(self):
    initial = super().get_initial()
    initial["tags"] = ", ".join(tag.name for tag in self.get_object().tags.all())
    return initial

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('comment_form', CommentForm())
        # comments are available as post.comments.all() thanks to related_name
        return context

    # handle inline comment submission (POST to same URL)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('blog:login')  # or return HttpResponseForbidden()

        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect(self.object.get_absolute_url() + '#comments')  # jump to comments
        # if form invalid, re-render detail with form errors
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url() + '#comment-{}'.format(self.object.pk)

    def test_func(self):
        return self.get_object().author == self.request.user

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        return self.get_object().author == self.request.user    
    
# add this CommentCreateView class to blog/views.py

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'   # create this template if you haven't
    # you can optionally set success_url here, but we build it dynamically

    def dispatch(self, request, *args, **kwargs):
        """
        Capture post_id from URL and store the Post instance for use in form_valid.
        """
        self.post = get_object_or_404(Post, pk=kwargs.get('post_id'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Fill in author and post before saving.
        """
        form.instance.author = self.request.user
        form.instance.post = self.post
        return super().form_valid(form)

    def get_success_url(self):
        """
        After creating a comment, redirect back to the post detail.
        """
        return self.post.get_absolute_url() + '#comment-{}'.format(self.object.pk)

def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)
    return render(request, "blog/posts_by_tag.html", {
        "posts": posts,
        "tag": tag_name
    })