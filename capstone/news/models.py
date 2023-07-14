from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    if_journalist = models.BooleanField(default=False)


def validate_introduction(value):
    sentences = value.split('.')
    num_sentences = len(sentences)
    if num_sentences > 3:
        raise ValidationError(
            _('Introduction should be limited to three sentences or less.')
        )


class Post_Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Post_Category'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Post_Category, on_delete=models.CASCADE)
    if_trending = models.BooleanField(default=False)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/')
    introduction = models.TextField(validators=[validate_introduction])
    details = models.TextField()
    admin_evaluation = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Post'



class ApprovedPost(models.Model):
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, null=True)
    time_posted = models.DateTimeField(auto_now_add=True)
    # additional fields for approved liwanag posts

    @classmethod
    def create_from_draft(cls, post):
        approved_post = cls.objects.create(post=post)
        return approved_post

    def __str__(self):
        return f"ApprovedPost: {self.post}"

