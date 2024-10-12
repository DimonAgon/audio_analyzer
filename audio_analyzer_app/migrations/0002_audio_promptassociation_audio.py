# Generated by Django 5.1.2 on 2024-10-11 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_analyzer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('audio', models.FileField(upload_to='audios/')),
            ],
        ),
        migrations.AddField(
            model_name='promptassociation',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prompt_association', to='audio_analyzer_app.audio'),
        ),
    ]
