from django.db import models

class Entry(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    income_expense = models.BooleanField()
    amount = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=50)

class Repeat(models.Model):
    repeat = models.BooleanField()
    date = models.DateField()
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)

class EntryTag(models.Model):
    entry = models.ForeignKey('Entry', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
