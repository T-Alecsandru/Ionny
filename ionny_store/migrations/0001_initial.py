# Generated by Django 4.0.2 on 2022-02-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(default='static/not_available.png', upload_to='static/product_images/')),
                ('promoted', models.BooleanField(default=False)),
            ],
        ),
    ]
