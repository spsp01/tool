# Generated by Django 2.0.5 on 2018-07-18 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='RaportScreaming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_crawled', models.DateField()),
                ('total_url_encountered', models.IntegerField()),
                ('total_url_crawled', models.IntegerField()),
                ('client', models.ForeignKey(on_delete='Cascade', to='tool.Client')),
            ],
        ),
    ]
