from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=500)
    pub_date = models.DateField()

    def __str__(self):
        return self.title
