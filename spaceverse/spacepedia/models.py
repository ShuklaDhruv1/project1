from django.db import models

# Create your models here.
from django.db import models

class SpaceTopic(models.Model):
    TOPIC_TYPES = [
        ('PLANET', 'Planet'),
        ('STAR', 'Star'),
        ('COSMOLOGY', 'Cosmology'),
        ('GALAXY', 'Galaxy'),
        ('MISSION', 'Mission'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    topic_type = models.CharField(max_length=20, choices=TOPIC_TYPES)
    summary = models.CharField(max_length=300)
    content = models.TextField()

    class Meta:
        ordering = ['topic_type', 'title']

    def __str__(self):
        return f"{self.title} ({self.topic_type})"