# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
            ],
        ),
    ]
