# Generated by Django 5.1.3 on 2024-12-02 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0007_emprunteur_empruntpossible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprunteur',
            name='EmpruntPossible',
        ),
    ]
