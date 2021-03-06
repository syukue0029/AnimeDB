# Generated by Django 3.0.4 on 2020-03-27 02:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('place', models.CharField(max_length=200, verbose_name='保管場所')),
                ('type', models.IntegerField(choices=[(1, 'TVアニメ'), (2, '劇場アニメ')], default=1, verbose_name='TV/映画')),
                ('media', models.IntegerField(choices=[(1, 'BD'), (2, 'DVD')], default=1, verbose_name='メディア形式')),
                ('year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1963)], verbose_name='制作年')),
                ('epsode_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='話数')),
                ('media_number', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='巻数')),
                ('production', models.CharField(max_length=200, verbose_name='制作会社')),
                ('voiceactor', models.CharField(max_length=200, verbose_name='主演声優')),
                ('director', models.CharField(max_length=200, verbose_name='監督')),
                ('memo', models.TextField(blank=True, max_length=300, null=True, verbose_name='備考')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
            ],
            options={
                'verbose_name': 'アイテム',
                'verbose_name_plural': 'アイテム',
            },
        ),
    ]
