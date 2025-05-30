from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Eski tekli image alanı kaldırılmadı, geriye dönük uyumluluk için bırakıldı
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    def __str__(self):
        return f"Image for {self.post.title}"

class About(models.Model):
    title = models.CharField(max_length=100, default="Hakkımda")
    content = models.TextField()

    def __str__(self):
        return self.title