# Generated by Django 5.1.1 on 2024-12-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babyapp', '0006_alter_babyevent_sleep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baby',
            name='age',
            field=models.IntegerField(default=0, max_length=3),
        ),
    ]
