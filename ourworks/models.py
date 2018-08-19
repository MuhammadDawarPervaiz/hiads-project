from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Work(models.Model):
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = 'images/')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.title