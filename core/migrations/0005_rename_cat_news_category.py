# Generated by Django 4.1.7 on 2023-03-06 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_setting_options_remove_news_author_news_cat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='cat',
            new_name='category',
        ),
    ]