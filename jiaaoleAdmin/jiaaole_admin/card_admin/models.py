from django.db import models
from .common import *


class TbPmInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    pm_id = models.IntegerField(db_column='PM_ID')
    pm_name = models.CharField(db_column='PM_Name', max_length=40)
    type1 = models.CharField(db_column='Type1', max_length=10)
    type2 = models.CharField(db_column='Type2', max_length=10, blank=True, null=True)
    pm_form = models.CharField(db_column='PM_Form', max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.pm_id}_{self.pm_name}_{self.pm_form}_{self.type1}_{self.type2}"

    class Meta:
        managed = True
        db_table = 'tb_pm_info'
        unique_together = ('pm_id', 'pm_form')


class TbMoveInfo(models.Model):
    move_id = models.AutoField(db_column='Move_ID', primary_key=True)
    move_name = models.CharField(db_column='Move_Name', max_length=20)
    move_type = models.CharField(db_column='Move_Type', max_length=10)
    move_power = models.IntegerField(db_column='Move_Power', blank=True, null=True)
    accuracy = models.IntegerField(db_column='Accuracy')
    is_zmove = models.BooleanField(db_column='Is_ZMove')

    def __str__(self):
        return f"{self.move_name}_{self.move_power}_{self.move_type}"

    class Meta:
        managed = True
        db_table = 'tb_move_info'
        unique_together = ('move_name', 'move_power', 'move_type')


class TbCardInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    card_id = models.CharField(db_column='Card_ID', max_length=10)
    season_id = models.IntegerField(db_column='Season_ID', blank=True, null=True)
    energy = models.IntegerField(db_column='Energy')
    star = models.IntegerField(db_column='Star', blank=True, null=True)
    move1_id = models.ForeignKey(TbMoveInfo, on_delete=models.DO_NOTHING, related_name='Move1')
    move2_id = models.ForeignKey(TbMoveInfo, on_delete=models.DO_NOTHING, related_name='Move2', blank=True,
                                 null=True)
    zmove_id = models.ForeignKey(TbMoveInfo, on_delete=models.DO_NOTHING, related_name='ZMove', blank=True,
                                 null=True)
    hp = models.IntegerField(db_column='HP')
    attack = models.IntegerField(db_column='Attack')
    sp_attack = models.IntegerField(db_column='SP_Attack')
    defense = models.IntegerField(db_column='Defense')
    sp_defense = models.IntegerField(db_column='SP_Defense')
    speed = models.IntegerField(db_column='Speed')
    sp_system = models.IntegerField(db_column='SP_System', blank=True, null=True,
                                    db_comment='1: Mega进化 2: Z招式 4: 合体 8: 双重冲击 16: 连续冲击')
    pm_info = models.ForeignKey(TbPmInfo, on_delete=models.DO_NOTHING, related_name='PM')

    def get_season_display(self):
        return common_escaped(self.season_id, season_choice)

    def get_sp_system_display(self):
        return common_escaped(self.sp_system, sp_system_choice)

    def __str__(self):
        return f"{self.season_id}_{self.star}_{self.card_id}_{self.pm_info}"

    class Meta:
        managed = True
        db_table = 'tb_card_info'


class TbOrderColumn(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    season_id = models.IntegerField(db_column='Season_ID')
    display_name = models.IntegerField(db_column='Display_Name')

    def __str__(self):
        return f"{self.season_id}_{self.display_name}"

    class Meta:
        managed = True
        db_table = 'tb_order_column'
        unique_together = ('season_id', 'display_name')


class TbOrderDetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    column_id = models.ForeignKey(TbOrderColumn, on_delete=models.DO_NOTHING, related_name='Column_ID')
    card_id = models.ForeignKey(TbCardInfo, on_delete=models.DO_NOTHING, related_name='Card_ID')
    order_position = models.IntegerField(db_column='Order_Position')

    def __str__(self):
        return f"{self.column_id}_{self.order_position}_{self.card_id}"

    class Meta:
        managed = True
        db_table = 'tb_order_detail'
        unique_together = ('column_id', 'order_position')
