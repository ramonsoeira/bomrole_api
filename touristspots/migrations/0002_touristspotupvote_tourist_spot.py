# Generated by Django 3.0.3 on 2020-02-08 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('touristspots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspotupvote',
            name='tourist_spot',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE,
                                    to='touristspots.TouristSpot'),
            preserve_default=False,
        ),
    ]
