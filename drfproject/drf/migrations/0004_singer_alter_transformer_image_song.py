# Generated by Django 4.1 on 2022-11-12 11:35

from django.db import migrations, models
import django.db.models.deletion
import drf.models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0003_transformer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='transformer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=drf.models.upload_to),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('duration', models.IntegerField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sung_by', to='drf.singer')),
            ],
        ),
    ]
