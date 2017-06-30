# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20151021_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='notified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='deactivation_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='idea',
            name='deactivation_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='initiative',
            name='community_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='initiative',
            name='site_url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='initiative',
            name='survey_url',
            field=models.URLField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='socialnetworkappuser',
            name='registration_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 18, 47, 42, 622179, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialnetworkappuser',
            name='welcome_msg_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vote',
            name='deactivation_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='platform',
            field=models.ForeignKey(to='app.ConsultationPlatform'),
        ),
        migrations.AlterField(
            model_name='socialnetworkapp',
            name='community',
            field=models.ForeignKey(blank=True, to='app.SocialNetworkAppCommunity', null=True),
        ),
    ]
