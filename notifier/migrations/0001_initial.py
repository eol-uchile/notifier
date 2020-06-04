# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumDigestTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_dt', models.DateTimeField(help_text=b'Beginning of time slice for which to send forum digests.')),
                ('to_dt', models.DateTimeField(help_text=b'End of time slice for which to send forum digests.')),
                ('node', models.CharField(help_text=b'Name of node that scheduled the task.', max_length=255, blank=True)),
                ('created', models.DateTimeField(help_text=b'Time at which the task was scheduled.', auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MappOrg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization', models.CharField(unique=True, max_length=50, db_index=True)),
                ('url_site', models.CharField(max_length=150)),
                ('url_logo', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='forumdigesttask',
            unique_together=set([('from_dt', 'to_dt')]),
        ),
    ]
