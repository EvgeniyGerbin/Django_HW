from django.db import models




class Author(models.Model):
    first_name = models.CharField('Name', max_length=32)
    last_name = models.CharField('Surname', max_length=32)

    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = 'Author'

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


class Book(models.Model):
    title = models.CharField("Book Title", max_length=32)
    author = models.OneToOneField('Book_Catalog.Author', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Books"
        verbose_name_plural = 'Book'

    def __str__(self):
        return f'{self.title} by {self.author}'

