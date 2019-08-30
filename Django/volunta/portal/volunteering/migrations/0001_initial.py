# Generated by Django 2.2.3 on 2019-07-24 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.IntegerField(choices=[(1, 'Health'), (2, 'Nutrition'), (3, 'Education')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('place', models.CharField(max_length=150)),
                ('requirements', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteering.Activity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteering.Organization'),
        ),
    ]