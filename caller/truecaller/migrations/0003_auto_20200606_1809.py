# Generated by Django 3.0.7 on 2020-06-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truecaller', '0002_spam_usercontacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam',
            name='spam',
            field=models.IntegerField(unique=True),
        ),
    ]
