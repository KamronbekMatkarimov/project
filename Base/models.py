from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200, default="Здравствуйте")
    subtitle = models.CharField(max_length=200, default="Меня зовут Камрон")
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='home/', blank=True, null=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    color = models.CharField(max_length=7, default="#7127BA")  # HEX color

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
