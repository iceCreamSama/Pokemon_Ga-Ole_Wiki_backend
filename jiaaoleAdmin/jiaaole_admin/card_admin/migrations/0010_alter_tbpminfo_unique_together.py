# Generated by Django 4.2.6 on 2023-10-20 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_admin', '0009_remove_tbcardinfo_pm_form_remove_tbcardinfo_pm_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tbpminfo',
            unique_together={('pm_id', 'pm_form')},
        ),
    ]
