# Generated by Django 5.1.1 on 2024-09-17 20:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0005_alter_categoria_categoria_alter_examen_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examen',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6c65efec-7535-11ef-8537-f0038c90f80e'), primary_key=True, serialize=False),
        ),
    ]
