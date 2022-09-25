# Generated by Django 4.1.1 on 2022-09-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_service_service_icon_alter_service_service_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfoCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_heading', models.CharField(max_length=50)),
                ('info_count', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
