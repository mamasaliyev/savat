from django.db import models
from register.models import CustomUser

class Mahsulot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", null=True, blank=True)  # Standart qiymat bo'sh matn
    price = models.IntegerField()
    image = models.ImageField(upload_to='mahsulot_images/', null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.miqdor} x {self.mahsulot.id}"
