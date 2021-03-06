# Generated by Django 2.1 on 2018-11-11 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_name', models.CharField(max_length=200)),
                ('res_address', models.CharField(max_length=200)),
                ('res_description', models.CharField(max_length=400)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.City')),
            ],
        ),
    ]
