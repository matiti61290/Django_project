# Generated by Django 5.1.3 on 2024-11-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0005_alter_items_emprunteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='dateEmprunt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
