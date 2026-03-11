from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)#we do not put parenthesis at the end of the now as we donot want to carry out that function at that moment
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
        

