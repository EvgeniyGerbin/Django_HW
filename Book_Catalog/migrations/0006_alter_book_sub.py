# Generated by Django 4.0.1 on 2022-01-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Catalog', '0005_book_sub_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='sub',
            field=models.ManyToManyField(related_name='SubAuthors', to='Book_Catalog.Author'),
        ),
    ]
