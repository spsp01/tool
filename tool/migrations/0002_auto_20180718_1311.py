# Generated by Django 2.0.5 on 2018-07-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='raportscreaming',
            name='external_blocked_by_robots',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='raportscreaming',
            name='internal_blocked_by_robots',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]