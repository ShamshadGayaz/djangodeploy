from django.db import models


class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='home_content/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Home Content'
        verbose_name_plural = 'Home Contents'

    def __str__(self):
        return self.title
