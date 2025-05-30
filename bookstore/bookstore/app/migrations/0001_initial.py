# Generated by Django 5.1.6 on 2025-04-30 05:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('bookid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Programming', 'Programming'), ('Database', 'Database'), ('Networking', 'Networking')], max_length=50)),
                ('price', models.FloatField()),
                ('qut', models.PositiveIntegerField(default=0)),
                ('dop', models.DateField()),
                ('userid', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
