from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Profile model to extend user information
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Removed for now
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    about = models.TextField(max_length=500, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    program_type = models.CharField(max_length=100, null=True, blank=True)
    grad_year = models.IntegerField(null=True, blank=True)
    portfolio_url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="profile_images/", blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    program_type = models.CharField(max_length=100, null=True, blank=True)
    grad_year = models.IntegerField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # TODO: Update once details view is created
    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})

class Comment(models.Model):
    content = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'