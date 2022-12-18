from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profil(models.Model):
    objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 200:
            new_img = (300, 200)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
