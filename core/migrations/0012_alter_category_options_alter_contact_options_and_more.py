# Generated by Django 4.1.7 on 2023-04-02 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_category_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kateqoryalar'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Elaqe', 'verbose_name_plural': 'Əlaqələr'},
        ),
        migrations.AlterModelOptions(
            name='doctors',
            options={'verbose_name': 'Hekim', 'verbose_name_plural': 'Hekimler'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Xeberler', 'verbose_name_plural': 'Xeberler'},
        ),
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Ayarlar', 'verbose_name_plural': 'Ayarlar'},
        ),
        migrations.RemoveField(
            model_name='setting',
            name='address1_az',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='address1_en',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='address2_az',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='address2_en',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='creator_az',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='creator_en',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='number1_az',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='number1_en',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='number2_az',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='number2_en',
        ),
    ]
