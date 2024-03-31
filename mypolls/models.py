from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mypolls_posts')

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    class Question(models.Model):
        # model fields

        class Meta:
            app_label = 'mypolls'

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.title

        # Add an indented block of code here


    def __str__(self):
        return self.question_text

