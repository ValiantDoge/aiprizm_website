# Generated by Django 4.1.1 on 2022-09-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member_pic', models.ImageField(default='', upload_to='website/images')),
                ('team_member_name', models.CharField(max_length=50)),
                ('team_member_desc', models.CharField(max_length=50)),
                ('team_member_twitter', models.URLField(default='', max_length=300)),
                ('team_member_facebook', models.URLField(default='', max_length=300)),
                ('team_member_instagram', models.URLField(default='', max_length=300)),
                ('team_member_stackoverflow', models.URLField(default='', max_length=300)),
                ('team_member_linkedin', models.URLField(default='', max_length=300)),
            ],
        ),
    ]