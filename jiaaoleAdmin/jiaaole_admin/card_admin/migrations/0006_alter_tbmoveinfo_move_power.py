# Generated by Django 4.2.6 on 2023-10-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_admin', '0005_alter_tbcardinfo_move1_id_alter_tbcardinfo_move2_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbmoveinfo',
            name='move_power',
            field=models.IntegerField(blank=True, db_column='Move_Power', null=True),
        ),
    ]