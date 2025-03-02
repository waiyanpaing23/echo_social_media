from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_img = models.ImageField(upload_to='profile_images/', default='profile_images/profile.jpg')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
class Friend(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return f'{self.user1.username} & {self.user2.username}'