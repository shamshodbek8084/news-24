# Generated by Django 5.0 on 2024-09-12 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
