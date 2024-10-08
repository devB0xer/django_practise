# Generated by Django 5.1.1 on 2024-09-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('someapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dateOfBirth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='bool',
            name='year',
            field=models.DateField(null=True),
        ),
    ]
