from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cse(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    qnt=models.IntegerField()
    def __str__(self):
        return self.name
class Ece(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    qnt=models.IntegerField()
    def __str__(self):
        return self.name
class Eee(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    qnt=models.IntegerField()
    def __str__(self):
        return self.name
class Civil(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    qnt=models.IntegerField()
    def __str__(self):
        return self.name
class Mech(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    qnt=models.IntegerField()
    def __str__(self):
        return self.name


class Cart(models.Model):
    clgid=models.CharField(max_length=100)
    bookid=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    datecompleted = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.clgid



class Memo(models.Model):
    img=models.ImageField(upload_to='pics')
class All(models.Model):
    url=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')