# Generated by Django 3.1.6 on 2021-02-09 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shop', '0002_auto_20210209_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='categories',
            field=models.ManyToManyField(related_name='Categories', to='e_shop.Category'),
        ),
    ]
