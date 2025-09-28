from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50,null=False, blank=False)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    name = models.CharField(max_length=20,ull=False, blank=False)

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=20,null=False, blank=False)

    def __str__(self):
        return self.name
