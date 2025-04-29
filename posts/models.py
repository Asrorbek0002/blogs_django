from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    cover = models.ImageField(upload_to="images/", null=True, blank=True)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Model<{self.title}>"
