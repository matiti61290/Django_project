# Generated by Django 5.1.3 on 2024-11-29 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliothecaire', '0004_alter_emprunteur_nombreemprunt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliothecaire.emprunteur'),
        ),
    ]
