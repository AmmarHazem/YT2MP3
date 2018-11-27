from django.db import models




class YoutubeLink(models.Model):
    url = models.URLField()
    title = models.CharField(max_length = 255, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp', 'title')
