from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=75)
    book_review = models.CharField(max_length=500)
    book_pages = models.IntegerField()

    def __str__(self):
        return self.book_name + ' - ' + self.book_review + ' - ' + str(self.book_pages)


class User(models.Model):
    user_name = models.CharField(max_length=75)
    user_mail = models.EmailField()

    def __str__(self):
        return self.user_name + ' - ' + self.user_mail 


class Authors(models.Model):
    author_name = models.CharField(max_length=75)
    author_mail = models.EmailField()

    def __str__(self):
        return self.author_name + ' - ' + self.author_mail 

