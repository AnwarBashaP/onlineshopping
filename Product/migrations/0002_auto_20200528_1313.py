# Generated by Django 3.0.4 on 2020-05-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='AvalibleNo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdetails',
            name='Description',
            field=models.TextField(default='', verbose_name='Descriptions'),
            preserve_default=False,
        ),
    ]
