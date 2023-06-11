# Generated by Django 4.2.2 on 2023-06-11 10:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='seller',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('transport_manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draft.transporter')),
            ],
        ),
        migrations.CreateModel(
            name='PickupAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='draft.seller')),
            ],
        ),
        migrations.AddConstraint(
            model_name='vehicle',
            constraint=models.UniqueConstraint(fields=('category', 'transport_manager_id'), name='unique_vehicle'),
        ),
    ]