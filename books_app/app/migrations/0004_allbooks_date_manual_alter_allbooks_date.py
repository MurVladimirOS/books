# Generated by Django 4.2 on 2023-04-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_allbooks_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='allbooks',
            name='date_manual',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Manual date'),
        ),
        migrations.AlterField(
            model_name='allbooks',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date creating'),
        ),
    ]
