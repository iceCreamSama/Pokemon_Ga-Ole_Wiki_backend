# Generated by Django 4.2.6 on 2023-10-20 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card_admin', '0006_alter_tbmoveinfo_move_power'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbPmInfo',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('pm_id', models.IntegerField(db_column='PM_ID')),
                ('pm_name', models.CharField(db_column='PM_Name', max_length=40)),
                ('type1', models.CharField(db_column='Type1', max_length=10)),
                ('type2', models.CharField(blank=True, db_column='Type2', max_length=10, null=True)),
                ('pm_form', models.CharField(blank=True, db_column='PM_Form', max_length=10, null=True)),
            ],
            options={
                'db_table': 'tb_pm_info',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='tbcardinfo',
            name='pm_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='PM', to='card_admin.tbpminfo'),
        ),
    ]
