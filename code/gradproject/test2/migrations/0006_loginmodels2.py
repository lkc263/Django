# Generated by Django 3.2 on 2021-05-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0005_alter_loginmodels_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginModels2',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=45)),
                ('username2', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'test2_loginmodels',
                'managed': False,
            },
        ),
    ]