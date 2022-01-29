from django.db import models

import myapp.models


class Author(models.Model):
    first_name = models.CharField('Name', max_length=32)
    last_name = models.CharField('Surname', max_length=32)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


class Book(models.Model):
    title = models.CharField('Book Title', max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Author')
    sub = models.ManyToManyField(Author, related_name='Subs', verbose_name='Sub Authors', )

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = 'Books'

    def __str__(self):
        return f'{self.title} by {self.author}'


class Reader(models.Model):
    user = models.ForeignKey(myapp.models.Article, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='reader')
    is_own = models.BooleanField('Book taken', default=True)

    def __str__(self):
        return f'{self.user} own {self.book}'



