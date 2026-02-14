from django.db import models
from embed_video.fields import EmbedVideoField


class DrawerItem(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to='drawer_images/', null=True, blank=True)
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
