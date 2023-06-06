from django.db import models
from users.models import User

class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    is_published = models.BooleanField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="ad_images", null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.username



