# Generated by Django 2.1.1 on 2018-10-31 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_tex',
            new_name='question_text',
        ),
    ]