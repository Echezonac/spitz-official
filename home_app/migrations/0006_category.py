# Generated by Django 4.0.3 on 2022-09-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_alter_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Event', max_length=100)),
            ],
        ),
    ]
