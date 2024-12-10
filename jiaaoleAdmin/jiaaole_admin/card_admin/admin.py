from django.contrib import admin
from .models import TbCardInfo, TbMoveInfo, TbOrderColumn, TbOrderDetail, TbPmInfo
from django import forms
from .common import *
import logging


# Register your models here.
class PMForm(forms.ModelForm):
    class Meta:
        model = TbPmInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type1'].widget = forms.Select(choices=type_choice)
        self.fields['type2'].widget = forms.Select(choices=type_choice)


class PMAdmin(admin.ModelAdmin):
    fields = [
        ('pm_id', 'pm_name'), ('type1', 'type2', 'pm_form')
    ]
    form = PMForm

    list_display = ('pm_id', 'pm_name', 'type1', 'type2', 'pm_form')
    list_filter = ('type1', 'type2')


class CardForm(forms.ModelForm):
    class Meta:
        model = TbCardInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['season_id'].widget = forms.Select(choices=season_choice)
        self.fields['star'].widget = forms.Select(choices=star_choice)
        self.fields['sp_system'].widget = forms.Select(choices=sp_system_choice)


class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('基本信息', {'fields': [('season_id', 'card_id', 'star', 'energy', 'pm_info')]}),
        ('战斗信息', {
            'fields': [('hp', 'attack', 'sp_attack', 'defense', 'sp_defense', 'speed'),
                       ('move1_id', 'move2_id', 'zmove_id'), 'sp_system']})
    ]
    form = CardForm

    list_display = (
        'id', 'get_season_display', 'card_id', 'pm_info', 'star', 'get_sp_system_display', 'energy', 'hp', 'attack',
        'sp_attack', 'defense', 'sp_defense', 'speed', 'move1_id', 'zmove_id')
    list_filter = ('season_id', 'star', 'sp_system')


class MoveForm(forms.ModelForm):
    class Meta:
        model = TbMoveInfo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['move_type'].widget = forms.Select(choices=type_choice)


class MoveAdmin(admin.ModelAdmin):
    fields = [
        ('move_name', 'is_zmove'), ('move_type', 'move_power', 'accuracy')
    ]
    form = MoveForm

    @staticmethod
    def type_escaped(obj):
        return common_escaped(obj.move_type, type_choice)

    list_display = ('move_name', 'is_zmove', 'type_escaped', 'move_power', 'accuracy')
    list_filter = ('is_zmove', 'move_type')


class OrderForm(forms.ModelForm):
    class Meta:
        model = TbOrderColumn
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['season_id'].widget = forms.Select(choices=season_choice)


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm


class DetailAdmin(admin.ModelAdmin):
    list_filter = ('column_id',)


admin.site.register(TbPmInfo, PMAdmin)
admin.site.register(TbCardInfo, CardAdmin)
admin.site.register(TbMoveInfo, MoveAdmin)
admin.site.register(TbOrderColumn, OrderAdmin)
admin.site.register(TbOrderDetail, DetailAdmin)
