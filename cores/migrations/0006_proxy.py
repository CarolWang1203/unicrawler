# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cores', '0005_auto_20160130_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind', models.IntegerField(default=1, verbose_name=b'\xe4\xbb\xa3\xe7\x90\x86\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(0, b'\xe9\x80\x8f\xe6\x98\x8e\xe4\xbb\xa3\xe7\x90\x86'), (1, b'\xe9\xab\x98\xe5\xba\xa6\xe5\x8c\xbf\xe5\x90\x8d')])),
                ('user', models.CharField(default=b'', max_length=100, blank=True)),
                ('password', models.CharField(default=b'', max_length=100, blank=True)),
                ('host', models.CharField(max_length=100)),
                ('port', models.IntegerField(default=80)),
                ('address', models.CharField(default=b'', max_length=100, verbose_name=b'\xe5\x9c\xb0\xe7\x90\x86\xe4\xbd\x8d\xe7\xbd\xae', blank=True)),
                ('speed', models.IntegerField(default=0, verbose_name=b'\xe8\xbf\x9e\xe6\x8e\xa5\xe9\x80\x9f\xe5\xba\xa6(ms)')),
                ('status', models.IntegerField(default=0, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe6\x9c\xaa\xe6\xa3\x80\xe6\xb5\x8b'), (1, b'\xe6\xa3\x80\xe6\xb5\x8b\xe6\x88\x90\xe5\x8a\x9f'), (2, b'\xe6\xa3\x80\xe6\xb5\x8b\xe5\xa4\xb1\xe8\xb4\xa5')])),
                ('retry', models.IntegerField(default=0, verbose_name=b'\xe5\xb0\x9d\xe8\xaf\x95\xe6\xac\xa1\xe6\x95\xb0')),
            ],
            options={
                'verbose_name_plural': '\u8bbf\u95ee\u4ee3\u7406',
            },
        ),
    ]
