from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200, default="Здравствуйте")
    subtitle = models.CharField(max_length=200, default="Меня зовут Камрон")
    description = models.TextField(blank=True, default="")
    image = models.ImageField(upload_to='home/', blank=True, null=True)

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="Описание пока отсутствует")
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    icon_class = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    