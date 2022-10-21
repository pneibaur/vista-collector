from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# UPCOMING CATEGORY FEATURE
# TYPES = ('Beach', 'Mountain', 'Land', 'Sky', 'Star', 'City', 'Rural', 'Desert', 'Lake', 'Ocean', 'Frozen',)
# type = models.CharField(max_length=16, choices=TYPES, default=TYPES[2])

SEASONS = (
    ('WI','Winter',),
    ('SP', 'Spring',),
    ('SU', 'Summer',),
    ('FA', 'Fall',),
    )

class Flair(models.Model):
    tag = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("flair_detail", kwargs={"pk": self.id})

    def __str__(self) -> str:
        return self.tag
    

# Create your models here.
class Vista(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=2, choices=SEASONS, default=SEASONS[1][0])
    year = models.IntegerField()
    location = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    tags = models.ManyToManyField(Flair)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("vista_detail", kwargs={"vista_id": self.id})

    def season_display(self):
        return f"{self.get_season_display()}"
    

class Comment(models.Model):
    comment = models.TextField(max_length=250)
    date = models.DateField(auto_now_add=True)
    vista = models.ForeignKey(Vista, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    
    class Meta:
        ordering = ["-date"]

class Photo(models.Model):
    url = models.CharField(max_length=200)
    vista = models.ForeignKey(Vista, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for vista_id: {self.vista_id} @{self.url}."
