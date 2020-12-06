# Generated by Django 2.0.13 on 2020-12-06 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='followup_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_follow_up', models.DateField()),
                ('response', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='source_list',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source', models.CharField(max_length=200)),
                ('contact_person_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
                ('person_number', models.IntegerField()),
                ('current_stage', models.BooleanField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='followup_history',
            name='abc',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Lead_Management_app.source_list'),
        ),
    ]
