# Generated by Django 2.1.7 on 2019-03-05 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20190305_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
    ]