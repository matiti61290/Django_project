# Generated by Django 5.1.3 on 2024-11-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0003_jeudeplateau_createur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprunteur',
            name='NombreEmprunt',
            field=models.IntegerField(),
        ),
    ]
