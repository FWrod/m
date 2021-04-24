# Generated by Django 3.0.9 on 2021-04-23 21:55

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=18, unique=True)),
                ('staff', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('superuser', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Card title')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Card content')),
                ('image', models.TextField(blank=True, verbose_name='Image URL')),
                ('date', models.CharField(max_length=80, verbose_name='Card date')),
                ('favorites', models.ManyToManyField(related_name='card_favorited_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Card title')),
                ('deck_format', models.CharField(choices=[('STD', 'Standard'), ('MDN', 'Modern'), ('PIN', 'Pioneer'), ('HTC', 'Historic'), ('PPR', 'Pauper'), ('LGC', 'Legacy'), ('VTG', 'Vintage'), ('CMD', 'Commander')], max_length=3)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cards', models.ManyToManyField(related_name='Deck_cards', to='core.Card')),
                ('favorites', models.ManyToManyField(related_name='deck_favorited_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Related user')),
            ],
        ),
    ]
