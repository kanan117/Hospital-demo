# Generated by Django 4.1.7 on 2023-04-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalizRaporu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hasta_ad_soyad', models.CharField(max_length=100)),
                ('rapor', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
