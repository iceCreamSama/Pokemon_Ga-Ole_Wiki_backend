# Generated by Django 4.2.6 on 2023-10-20 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_admin', '0007_tbpminfo_tbcardinfo_pm_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbcardinfo',
            name='pm_id',
        ),
    ]