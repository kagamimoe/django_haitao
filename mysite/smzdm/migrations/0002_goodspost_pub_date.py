# encoding: utf8
from django.db import models, migrations
from datetime import date


class Migration(migrations.Migration):

    dependencies = [
        ('smzdm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodspost',
            name='pub_date',
            field=models.DateTimeField(default=date(2014, 9, 6), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
