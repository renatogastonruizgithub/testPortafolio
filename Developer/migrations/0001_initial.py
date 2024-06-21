# Generated by Django 5.0.2 on 2024-04-06 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True)),
                ('ciudad', models.CharField(max_length=200)),
                ('fechaNacimiento', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='media')),
                ('url_developer', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]