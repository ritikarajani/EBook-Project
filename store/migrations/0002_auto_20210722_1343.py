# Generated by Django 3.2.5 on 2021-07-22 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ebook',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
