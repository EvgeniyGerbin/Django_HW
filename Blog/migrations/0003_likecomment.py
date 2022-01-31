# Generated by Django 4.0.1 on 2022-01-30 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_commentpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.commentpost')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.bloger')),
            ],
        ),
    ]