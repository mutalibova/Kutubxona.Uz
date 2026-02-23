from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Badiiy', 'Badiiy'),
        ('Biznes', 'Biznes'),
        ('Darslik', 'Darslik'),
        ('Tarix', 'Tarix'),
    ]



    ktob = models.ImageField(upload_to='book/')
    nomi = models.CharField(max_length=200)
    Yozuvchi = models.CharField(max_length=200 )
    kategoriya = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    tavsifi = models.TextField(blank=True)
    rating = models.IntegerField(default=0)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    
    def __str__(self):
        return self.nomi
    
    


class Book1(models.Model):
    ktob1 = models.ImageField(upload_to='book/')
    nomi1 = models.CharField(max_length=200)
    Yozuvchi1 = models.CharField(max_length=200)
    tavsifi1 = models.TextField(blank=True)
    rating1 = models.IntegerField(default=0)
    pdf1 = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return self.nomi1