# Generated by Django 4.1.7 on 2023-03-10 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_blogs_delete_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
