# Generated by Django 4.1.1 on 2022-09-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('describtion', models.CharField(max_length=222)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('size', models.CharField(max_length=222)),
                ('grade', models.CharField(max_length=222)),
                ('quality', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1)),
                ('colours', models.CharField(choices=[('Gr', 'Grey'), ('Bu', 'Blue'), ('Bl', 'Black')], max_length=2)),
            ],
        ),
    ]
