# Generated by Django 2.1 on 2018-08-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_team_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
