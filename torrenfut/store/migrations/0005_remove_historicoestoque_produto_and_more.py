# Generated by Django 5.1.2 on 2024-10-30 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_historicoestoque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicoestoque',
            name='produto',
        ),
        migrations.AddField(
            model_name='historicoestoque',
            name='camiseta',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='historico_camisetas', to='store.camiseta'),
            preserve_default=False,
        ),
    ]
