# Generated by Django 5.2.1 on 2025-07-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_author_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dod',
            field=models.DateField(blank=True, null=True),
        ),
    ]
