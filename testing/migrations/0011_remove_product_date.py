# Generated by Django 5.0.2 on 2024-04-16 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0010_combo_combo_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]
