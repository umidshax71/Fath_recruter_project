from django.db import models
class Company(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='img', null=True ,blank=True)
    about = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to='file')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'
class Statistic(models.Model):
    name = models.CharField(max_length=200)
    count = models.PositiveIntegerField()
    about = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Statistic'
        verbose_name_plural = 'Statistic'
class Service(models.Model):
    image = models.ImageField(upload_to='img',null=True,blank=True)
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural ='Service'
class PlayList(models.Model):
    cost = models.IntegerField()
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'PlayList'
        verbose_name_plural = 'PlayList'
class Clients(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    def __str__(self):
        return self.name 
class Position(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Team(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} | {self.position}"
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'
class Contact(models.Model):
    location = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    social = models.CharField(max_length=200)
    facebook = models.CharField(max_length=2000)
    instagram = models.CharField(max_length=2000)
    telegram = models.CharField(max_length=2000)
    linkedin = models.CharField(max_length=2000)
    email = models.EmailField(null=True,blank=True)
    def __str__(self):
        return self.address
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
class Blog(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name = 'Blog' 
        verbose_name_plural = 'Blog'       
class Portfolio(models.Model):
    image = models.ImageField(upload_to='img')
    name = models.CharField(max_length=200)
    description = models.TextField()
            
             