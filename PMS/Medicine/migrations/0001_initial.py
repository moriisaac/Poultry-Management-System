# Generated by Django 5.0.3 on 2024-04-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stage', models.CharField(max_length=100)),
                ('expiry_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supplier_name', models.CharField(max_length=100)),
                ('medicine_type', models.CharField(choices=[('Chicks', 'Chicks'), ('Broilers', 'Broilers'), ('Layers', 'Layers'), ('Other', 'Other')], max_length=100)),
            ],
        ),
    ]
