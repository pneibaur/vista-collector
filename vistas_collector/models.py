from django.db import models
from django.urls import reverse

# UPCOMING CATEGORY FEATURE
# TYPES = ('Beach', 'Mountain', 'Land', 'Sky', 'Star', 'City', 'Rural', 'Desert', 'Lake', 'Ocean', 'Frozen',)
# type = models.CharField(max_length=16, choices=TYPES, default=TYPES[2])

class Flair(models.Model):
    tag = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return self.tag
    

# Create your models here.
class Vista(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)
    year = models.IntegerField()
    location = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    tags = models.ManyToManyField(Flair)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vista_detail", kwargs={"vista_id": self.id})
    

class Comment(models.Model):
    comment = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)
    vista = models.ForeignKey(Vista, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    
    class Meta:
        ordering = ["-date"]