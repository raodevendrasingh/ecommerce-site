# Generated by Django 4.2.6 on 2023-11-24 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
