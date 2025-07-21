from django.db import models

# Create your models here.

class CompanyInfo(models.Model):
    name = models.CharField(max_length=100, default="Hi-Tech Engineering Services")
    description = models.TextField(default="With over 26 years of experience, Hi-Tech Engineering Services delivers top-quality elevator maintenance, overhauling, and modernization with a commitment to excellence and rapid response times.")
    phone_1 = models.CharField(max_length=20, default="031-2477499")
    phone_2 = models.CharField(max_length=20, default="02136369171")
    email = models.EmailField(default="info@hitechservices.com")
    address = models.TextField(default="Karachi, Pakistan")
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.name
