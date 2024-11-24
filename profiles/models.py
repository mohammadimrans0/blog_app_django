from django.db import models
from author.models import Author

# Create your models here.
class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return f"{self.author.name}'s Profile"