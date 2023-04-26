# Generated by Django 4.1.5 on 2023-02-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikiquote_app', '0004_remove_article_category_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(default=[], to='wikiquote_app.category'),
        ),
    ]
