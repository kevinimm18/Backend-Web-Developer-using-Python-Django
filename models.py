from django.db import models
from django.utils.text import slugify

# Create your models here.

class contact(models.Model):
    Email       = models.EmailField(max_length=120)
    Subject     = models.CharField(blank=True, null=True, max_length=120)
    Pesan       = models.TextField(blank=False, null=False, max_length=120)

class Content_List(models.Model):
    Judul       = models.CharField(max_length=255)
    Isi         = models.TextField()
    Kategori    = models.CharField(max_length=255)
    Published   = models.DateTimeField(auto_now_add=True)
    Updated     = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(blank=True, editable=False)
    
    # Kalau tidak ada ini, maka dia akan langsung save semua. Saat ada def save ini,
    # saat kita save dia akan memanggil slug, baru di save
    def save(self):
        self.slug = slugify(self.Judul)
        super().save()

    # 
    def __str__(self):
        return f"{self.id}. {self.Judul}"
