import mysql.connector
import json
import os


def query_db(query, data):
    result = None
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="19861202",
        database="jiaaolewiki"
    )
    cursor = conn.cursor()

    # 插入数据
    try:
        cursor.execute(query, data)
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        print('Error:{}'.format(err))
    finally:
        # 提交更改并关闭连接
        cursor.close()
        conn.close()
    return result


def build_move_json(mid):
    query = "SELECT * from tb_move_info where Move_ID = %s"
    res = query_db(query, (mid,))
    move_name, move_type, move_power, move_acc = res[0][1], res[0][2], res[0][3], res[0][4],
    if move_power == -1:
        move_power = '变化'
    if move_acc == 200:
        move_acc = '必中'
    return {'name': move_name, 'pow': move_power, 'acc': move_acc, 'type': move_type}


def build_card_json(sql_res):
    card_list = []
    for card in sql_res:
        card_json = {}
        card_json['id'], card_json['cardID'], season_id, card_json['eng'], card_json[
            'star'], move1_id, move2_id, zmove_id = card[0], card[1], card[2], card[3], card[4], card[5], card[6], card[
            7]
        season_dict = {1: '第一弹', 2: '第二弹', 3: '第三弹', 4: '第四弹', 5: '传说一弹', 6: '传说二弹',
                       7: '传说三弹', 8: '传说四弹', 9: '冲锋一弹', 10: '冲锋二弹', 11: '冲锋三弹', 12: '冲锋四弹', 13: '冲锋五弹',
                       14: '冲锋六弹', None: '无'}
        card_json['season'] = season_dict[season_id]
        star_dict = {1: '一星', 2: '二星', 3: '三星', 4: '四星', 5: '五星', None: '无'}
        card_json['star'] = star_dict[card_json['star']]
        card_json['hp'], card_json['atk'], card_json['spatk'], card_json['def'], card_json['spdef'], card_json[
            'spd'], sp_system = card[8], card[9], card[10], card[11], card[12], card[13], card[14]
        if card_json['atk'] == 0:
            card_json['atk'] = '-'
        if card_json['spatk'] == 0:
            card_json['spatk'] = '-'
        sp_sys_dict = {None: '无', 1: 'Mega进化', 2: 'Z招式', 4: '合体', 8: '双重冲击', 16: '冲锋连击',
                       9: 'Mega|双重'}
        card_json['spsys'] = sp_sys_dict[sp_system]
        card_json['name'], card_json['type1'], card_json['type2'] = card[18], card[19], card[20]
        if not card_json['type2']:
            card_json['type2'] = ''
        # 处理moves
        card_json['moves'] = []
        card_json['moves'].append(build_move_json(move1_id))
        if move2_id:
            card_json['moves'].append(build_move_json(move2_id))
        if zmove_id:
            card_json['moves'].append(build_move_json(zmove_id))
        card_json['active'] = True
        card_json['color'] = False
        card_list.append(card_json)
    return card_list


def build_top_list(sql_query, filename):
    _top_list = []
    _query = sql_query
    _res = query_db(query, ())
    _json_res = build_card_json(_res)
    _top_list.extend(_json_res)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(_top_list, f, ensure_ascii=False)


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # 处理全部卡牌
    cardAllInfo = []
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id where '
             'Season_ID is not NULL order by Season_ID desc,Star desc')
    res = query_db(query, ())
    json_res = build_card_json(res)
    cardAllInfo.extend(json_res)
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id where '
             'Season_ID is NULL')
    res = query_db(query, ())
    json_res = build_card_json(res)
    cardAllInfo.extend(json_res)

    # 将字典列表转化为json并输出到文件中
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(cardAllInfo, f, ensure_ascii=False)

    # 处理Top能量
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id order by '
             'tb_card_info.Energy desc LIMIT 100')
    build_top_list(query, 'topEng.json')

    # 处理Top体力
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id order by '
             'tb_card_info.HP desc LIMIT 100')
    build_top_list(query, 'topHP.json')

    # 处理Top攻击
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id order by '
             'tb_card_info.Attack desc LIMIT 100')
    build_top_list(query, 'topAtk.json')

    # 处理Top特攻
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id order by '
             'tb_card_info.SP_Attack desc LIMIT 100')
    build_top_list(query, 'topSPAtk.json')

    # 处理Top防御
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id order by '
             'tb_card_info.Defense desc LIMIT 100')
    build_top_list(query, 'topDfs.json')

    # 处理Top特防
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id order by '
             'tb_card_info.SP_Defense desc LIMIT 100')
    build_top_list(query, 'topSPDfs.json')

    # 处理Top速度
    query = ('SELECT * from tb_card_info join jiaaolewiki.tb_pm_info tpi on tpi.ID = tb_card_info.pm_info_id order by '
             'tb_card_info.Speed desc LIMIT 100')
    build_top_list(query, 'topSpd.json')

    query = 'SELECT * from tb_move_info where Move_Name!="unknown" order by Move_Power desc'
    res = query_db(query, ())
    move_list = []
    for i in res:
        move = {'name': i[1], 'type': i[2], 'power': i[3], 'acc': i[4], 'zmove': i[5], 'active': True}
        if move['power'] == -1:
            move['power'] = '变化'
        if move['acc'] == 200:
            move['acc'] = '必中'
        move['zmove'] = True if move['zmove'] else False
        move_list.append(move)
    with open('move.json', 'w', encoding='utf-8') as f:
        json.dump(move_list, f, ensure_ascii=False)
