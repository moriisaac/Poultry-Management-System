# Generated by Django 5.0.3 on 2024-03-22 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livefarm', '0002_financemodelaudit_remove_farm_owner_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PenHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('pen_number', models.IntegerField(unique=True)),
                ('pen_name', models.CharField(max_length=60)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Penhouse',
                'verbose_name_plural': 'Penhouse',
                'db_table': 'penhouse_model',
                'ordering': ['id'],
                'permissions': (('birds_manage_pen_house', 'Can manage pen house custom'),),
            },
        ),
        migrations.CreateModel(
            name='MortalityCull',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Mortality', 'Mortality'), ('Cull', 'Cull')], max_length=30)),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('pen_house', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='birds.penhouse', to_field='pen_number')),
            ],
            options={
                'verbose_name': 'Mortality/Cull',
                'verbose_name_plural': 'Mortality/Culls',
                'db_table': 'mortality_cull_model',
                'permissions': (('birds_can_manage_mortality_cull', 'Can manage mortality/culls custom'),),
            },
        ),
        migrations.CreateModel(
            name='MedicineFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Medicine', 'Medicine'), ('Feed', 'Feed')], max_length=30)),
                ('quantity', models.CharField(max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('pen_house', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='birds.penhouse', to_field='pen_number')),
            ],
            options={
                'verbose_name': 'Medicine/Feed',
                'verbose_name_plural': 'Medicine/Feed',
                'db_table': 'medicine_feed_model',
                'permissions': (('birds_manage_medicine_feed', 'Can manage medicine/feeds custom'),),
            },
        ),
        migrations.CreateModel(
            name='BirdsStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='livefarm.financemodel')),
                ('pen_house', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='birds.penhouse', to_field='pen_number')),
            ],
            options={
                'verbose_name': 'Birds Stock',
                'verbose_name_plural': 'Birds Stock',
                'db_table': 'birds_stock_model',
                'permissions': (('birds_manage_birds_stock', 'Can manage bird stock custom'),),
            },
        ),
    ]