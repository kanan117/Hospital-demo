# Generated by Django 4.1.7 on 2023-03-06 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_news_page_tag_newstag_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Site setting', 'verbose_name_plural': 'Site setting'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='author',
        ),
        migrations.AddField(
            model_name='news',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='stories')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
                ('tags', models.ManyToManyField(to='core.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
