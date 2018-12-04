# Generated by Django 2.1.2 on 2018-12-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0005_user1'),
    ]

    operations = [
        migrations.CreateModel(
            name='cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='pictures')),
            ],
            options={
                'db_table': 'cv',
            },
        ),
    ]
