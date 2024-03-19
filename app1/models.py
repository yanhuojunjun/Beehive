from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    gender = models.CharField(max_length=8, choices=[('male', 'Male'), ('female', 'Female')])
    email = models.EmailField()

    class Meta:
        db_table = 'User'


class Image(models.Model):
    IMAGE_TYPES = [
        ('addiction', 'addiction'),
        ('unhoused', 'unhoused'),
        ('diseases', 'diseases'),
        ('recovering alcoholic','recovering alcoholic')
    ]

    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=IMAGE_TYPES, default='other')
    location = models.CharField(max_length=100)
    time = models.DateTimeField()
    bio = models.TextField()
    picture = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'Image'
