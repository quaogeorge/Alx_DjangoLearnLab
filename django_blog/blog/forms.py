from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        max_length=2000,
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "avatar")

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Add tags separated by commas (e.g. django, python)"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()

        tag_names = self.cleaned_data["tags"]
        tag_list = [t.strip() for t in tag_names.split(',') if t.strip()]

        # Clear old tags
        post.tags.clear()

        # Create or get existing tags
        for tag_name in tag_list:
            tag_obj, _ = Tag.objects.get_or_create(name=tag_name.lower())
            post.tags.add(tag_obj)

        return post