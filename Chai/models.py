from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chai(models.Model):
    name = models.CharField(max_length=100)
    short_Description = models.CharField(max_length=200, default="")
    date_added = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='chai_images')
    description = models.TextField(default="")
    price= models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    CHAI_TYPE_OPTIONS = [
        ('gr', 'Green Tea'),
        ('bl', 'Black Tea'),
        ('mi', 'Milk Tea'),
        ('he', 'Herbal Tea'),
    ]
    
    type = models.CharField(max_length=2, choices=CHAI_TYPE_OPTIONS)

    def __str__(self):
        return self.name

class Chai_Review(models.Model):
    chai = models.ForeignKey(Chai, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review_text = models.TextField(default="")
    
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.chai.name} - {self.rating}"