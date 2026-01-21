from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    program_type = models.CharField(max_length=100, null=True, blank=True)
    grad_year = models.IntegerField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # TODO: Update once details view is created
    # def get_absolute_url(self):
    #     return reverse("post_detail", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.id})