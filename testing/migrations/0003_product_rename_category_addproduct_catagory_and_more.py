# Generated by Django 5.0.2 on 2024-02-26 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_addproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('catagory', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=40)),
                ('img', models.ImageField(upload_to='media/')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='addproduct',
            old_name='category',
            new_name='catagory',
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='img',
            field=models.ImageField(upload_to='media/'),
        ),
    ]