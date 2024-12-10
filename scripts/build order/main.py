import mysql.connector


def insert_to_db(query, data):
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
        conn.commit()
    except mysql.connector.Error as err:
        print('Error:{}'.format(err))
    finally:
        # 提交更改并关闭连接
        cursor.close()
        conn.close()


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


s1_dict = [ [ {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 5,
    "name": "雷吉奇卡斯"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 4,
    "name": "克雷色利亚",
    "lucky": 0
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 4,
    "name": "艾路雷朵"
}, {
    "rank": 4,
    "name": "皮卡丘",
    "lucky": 0
}, {
    "rank": 3,
    "name": "猫头夜鹰"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 3,
    "name": "顿甲"
}, {
    "rank": 4,
    "name": "雷电云(化身)"
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 3,
    "name": "烈咬陆鲨"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 4,
    "name": "MEGA巨钳螳螂"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 3,
    "name": "烈焰猴"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 3,
    "name": "烈焰猴"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 4,
    "name": "沙奈朵"
}, {
    "rank": 3,
    "name": "庞岩怪"
}, {
    "rank": 5,
    "name": "达克莱伊",
    "lucky": 0
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 3,
    "name": "罗丝雷朵"
}, {
    "rank": 4,
    "name": "土台龟"
}, {
    "rank": 4,
    "name": "罗丝雷朵"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 4,
    "name": "帝王拿波"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 3,
    "name": "帝王拿波"
} ], [ {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 4,
    "name": "怪力"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 3,
    "name": "沙奈朵"
}, {
    "rank": 5,
    "name": "达克莱伊",
    "lucky": 0
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 4,
    "name": "烈焰猴"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 4,
    "name": "MEGA巨钳螳螂"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 3,
    "name": "沼王"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 3,
    "name": "怪力"
}, {
    "rank": 3,
    "name": "暴鲤龙",
    "lucky": 0
}, {
    "rank": 3,
    "name": "心蝙蝠"
}, {
    "rank": 4,
    "name": "沙奈朵"
}, {
    "rank": 5,
    "name": "伊裴尔塔尔"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 3,
    "name": "帝王拿波"
}, {
    "rank": 3,
    "name": "庞岩怪"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 4,
    "name": "帝王拿波"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 3,
    "name": "帝王拿波"
}, {
    "rank": 4,
    "name": "雷电云(化身)"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 4,
    "name": "土地云(化身)"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 3,
    "name": "顿甲"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 4,
    "name": "谢米(天空)",
    "lucky": 0
} ], [ {
    "rank": 4,
    "name": "帝王拿波"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 3,
    "name": "怪力"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 3,
    "name": "艾路雷朵"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 5,
    "name": "电束木"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 4,
    "name": "雷电云(化身)"
}, {
    "rank": 4,
    "name": "皮卡丘",
    "lucky": 0
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 3,
    "name": "烈咬陆鲨"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 4,
    "name": "谢米(天空)",
    "lucky": 0
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 4,
    "name": "土地云(化身)"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 3,
    "name": "猫头夜鹰"
}, {
    "rank": 3,
    "name": "沙奈朵"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 5,
    "name": "拉帝亚斯 红"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 3,
    "name": "罗丝雷朵"
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 3,
    "name": "暴鲤龙",
    "lucky": 0
}, {
    "rank": 3,
    "name": "飞天螳螂"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 4,
    "name": "龙卷云(化身)"
}, {
    "rank": 4,
    "name": "怪力"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 4,
    "name": "罗丝雷朵"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 1,
    "name": "小小象"
} ], [ {
    "rank": 4,
    "name": "烈焰猴"
}, {
    "rank": 4,
    "name": "庞岩怪"
}, {
    "rank": 3,
    "name": "土台龟"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 5,
    "name": "基格尔德完全体",
    "lucky": 0
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 3,
    "name": "沼王"
}, {
    "rank": 4,
    "name": "皮卡丘",
    "lucky": 0
}, {
    "rank": 4,
    "name": "土地云(化身)"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 3,
    "name": "帝王拿波"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 4,
    "name": "庞岩怪"
}, {
    "rank": 3,
    "name": "沙奈朵"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 4,
    "name": "MEGA烈咬陆鲨"
}, {
    "rank": 3,
    "name": "艾路雷朵"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 3,
    "name": "罗丝雷朵"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 3,
    "name": "猫头夜鹰"
}, {
    "rank": 4,
    "name": "罗丝雷朵"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 3,
    "name": "飞天螳螂"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 5,
    "name": "哲尔尼亚斯"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 4,
    "name": "谢米(天空)",
    "lucky": 0
}, {
    "rank": 4,
    "name": "艾路雷朵"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
} ], [ {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 3,
    "name": "烈咬陆鲨"
}, {
    "rank": 3,
    "name": "烈焰猴"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 3,
    "name": "飞天螳螂"
}, {
    "rank": 5,
    "name": "谜拟Q",
    "lucky": 0
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 4,
    "name": "克雷色利亚",
    "lucky": 0
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 4,
    "name": "龙卷云(化身)"
}, {
    "rank": 3,
    "name": "心蝙蝠"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 4,
    "name": "庞岩怪"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 4,
    "name": "土台龟"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 3,
    "name": "土台龟"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 3,
    "name": "帝王拿波"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 4,
    "name": "土地云(化身)"
}, {
    "rank": 3,
    "name": "顿甲"
}, {
    "rank": 5,
    "name": "盖欧卡"
}, {
    "rank": 3,
    "name": "暴鲤龙",
    "lucky": 0
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 3,
    "name": "沼王"
}, {
    "rank": 4,
    "name": "烈焰猴"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 4,
    "name": "MEGA巨钳螳螂"
}, {
    "rank": 1,
    "name": "草苗龟"
} ], [ {
    "rank": 3,
    "name": "沙奈朵"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 5,
    "name": "拉帝欧斯 蓝"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 4,
    "name": "克雷色利亚",
    "lucky": 0
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 3,
    "name": "心蝙蝠"
}, {
    "rank": 3,
    "name": "艾路雷朵"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 3,
    "name": "土台龟"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 4,
    "name": "谢米(天空)",
    "lucky": 0
}, {
    "rank": 3,
    "name": "庞岩怪"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 3,
    "name": "暴鲤龙",
    "lucky": 0
}, {
    "rank": 3,
    "name": "沙奈朵"
}, {
    "rank": 4,
    "name": "MEGA烈咬陆鲨"
}, {
    "rank": 5,
    "name": "虚吾伊德"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 3,
    "name": "烈咬陆鲨"
}, {
    "rank": 4,
    "name": "庞岩怪"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 4,
    "name": "帝王拿波"
}, {
    "rank": 4,
    "name": "土台龟"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 4,
    "name": "罗丝雷朵"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 4,
    "name": "雷电云(化身)"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 2,
    "name": "毒蔷薇"
} ], [ {
    "rank": 4,
    "name": "克雷色利亚",
    "lucky": 0
}, {
    "rank": 3,
    "name": "烈咬陆鲨"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 3,
    "name": "烈焰猴"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 5,
    "name": "固拉多"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 4,
    "name": "龙卷云(化身)"
}, {
    "rank": 3,
    "name": "庞岩怪"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 4,
    "name": "艾路雷朵"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 4,
    "name": "沙奈朵"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 3,
    "name": "心蝙蝠"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 3,
    "name": "艾路雷朵"
}, {
    "rank": 3,
    "name": "暴鲤龙",
    "lucky": 0
}, {
    "rank": 4,
    "name": "MEGA巨钳螳螂"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 4,
    "name": "怪力"
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 3,
    "name": "土台龟"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 3,
    "name": "飞天螳螂"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 3,
    "name": "怪力"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 4,
    "name": "MEGA烈咬陆鲨"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 5,
    "name": "谜拟Q",
    "lucky": 0
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
} ], [ {
    "rank": 4,
    "name": "皮卡丘",
    "lucky": 0
}, {
    "rank": 1,
    "name": "波加曼"
}, {
    "rank": 4,
    "name": "艾路雷朵"
}, {
    "rank": 2,
    "name": "猛火猴"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 1,
    "name": "拉鲁拉丝"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 3,
    "name": "顿甲"
}, {
    "rank": 2,
    "name": "尖牙陆鲨"
}, {
    "rank": 3,
    "name": "猫头夜鹰"
}, {
    "rank": 3,
    "name": "沼王"
}, {
    "rank": 5,
    "name": "基格尔德完全体",
    "lucky": 0
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 3,
    "name": "艾路雷朵"
}, {
    "rank": 4,
    "name": "MEGA烈咬陆鲨"
}, {
    "rank": 1,
    "name": "小小象"
}, {
    "rank": 2,
    "name": "豪力"
}, {
    "rank": 2,
    "name": "树林龟"
}, {
    "rank": 1,
    "name": "滚滚蝙蝠"
}, {
    "rank": 3,
    "name": "罗丝雷朵"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 2,
    "name": "心蝙蝠"
}, {
    "rank": 5,
    "name": "MEGA烈空坐"
}, {
    "rank": 1,
    "name": "腕力"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 2,
    "name": "猫头夜鹰"
}, {
    "rank": 3,
    "name": "土台龟"
}, {
    "rank": 3,
    "name": "烈焰猴"
}, {
    "rank": 1,
    "name": "草苗龟"
}, {
    "rank": 4,
    "name": "龙卷云(化身)"
}, {
    "rank": 2,
    "name": "地幔岩"
}, {
    "rank": 4,
    "name": "沙奈朵"
}, {
    "rank": 3,
    "name": "怪力"
}, {
    "rank": 2,
    "name": "顿甲"
}, {
    "rank": 2,
    "name": "毒蔷薇"
}, {
    "rank": 1,
    "name": "小火焰猴"
}, {
    "rank": 2,
    "name": "波皇子"
}, {
    "rank": 2,
    "name": "奇鲁莉安"
}, {
    "rank": 2,
    "name": "沼王"
}, {
    "rank": 1,
    "name": "圆陆鲨"
}, {
    "rank": 3,
    "name": "暴鲤龙",
    "lucky": 0
}, {
    "rank": 4,
    "name": "烈焰猴"
}, {
    "rank": 1,
    "name": "乌波"
}, {
    "rank": 1,
    "name": "含羞苞"
}, {
    "rank": 1,
    "name": "石丸子"
}, {
    "rank": 4,
    "name": "土台龟"
}, {
    "rank": 1,
    "name": "咕咕"
}, {
    "rank": 4,
    "name": "怪力"
} ] ]

input_cache_dict = {}


def get_column(season_id, display_name):
    query = "SELECT id FROM tb_order_column WHERE season_id = %s and Display_Name = %s"
    res = query_db(query, (season_id, display_name))
    return res[0][0] if res else None


def insert_column(season_id, display_name):
    query = "INSERT into tb_order_column (Season_ID, Display_Name) VALUES (%s, %s)"
    insert_to_db(query, (season_id, display_name))


def get_exist_order(col_id: int, order_position):
    query = "SELECT card_id_id, ID from tb_order_detail WHERE column_id_id = %s and Order_Position = %s"
    res = query_db(query, (col_id, order_position))
    return res[0] if res else None


def get_card_by_id(card_id):
    query = ("SELECT tb_card_info.Card_ID, tpi.PM_Name, tpi.PM_Form from tb_card_info join jiaaolewiki.tb_pm_info tpi "
             "on tpi.ID = tb_card_info.pm_info_id WHERE tb_card_info.ID = %s")
    res = query_db(query, (card_id,))
    return res[0] if res else None


def fetch_card(season_id, display_order, col_id, star, pm_name):
    query = ("SELECT tb_card_info.ID, tpi.PM_Name, tpi.PM_Form FROM tb_card_info join jiaaolewiki.tb_pm_info tpi on "
             "tpi.ID = tb_card_info.pm_info_id WHERE Season_ID = %s and star = %s and tpi.PM_Name LIKE CONCAT('%', "
             "%s, '%')")
    res = query_db(query, (season_id, int(star), pm_name))
    if len(res) == 1:
        return res[0][0]
    else:
        print("Can't find exactly card for season {} column {} order {}".format(season_id, col_id, display_order))
        if len(res) > 1:
            for i in res:
                print("find card_id: {}, pm_name: {}, pm_form: {}, pm_name(json): {}".format(i[0], i[1], i[2], pm_name))
        else:
            print("Can't find card for pm_name(json): {}".format(pm_name))
            query = ("SELECT tci.ID, tci.Card_ID, tpi.PM_Name, tpi.PM_Form FROM tb_card_info as tci join "
                     "jiaaolewiki.tb_pm_info tpi on tpi.ID = tci.pm_info_id WHERE tci.Star = %s and tci.Season_ID = %s")
            tips_res = query_db(query, (star, season_id))
            for i in tips_res:
                print("Tips pm info: ID: {}, card_id: {}, name: {}, form: {}".format(i[0], i[1], i[2], i[3]))
        cache_key = '{}_{}'.format(star, pm_name)
        if cache_key in input_cache_dict:
            print('Read from cache! star: {}, pm_name: {}, cached_id: {}'.format(star, pm_name, input_cache_dict[cache_key]))
            card_id = input_cache_dict[cache_key]
        else:
            while True:
                try:
                    card_id = int(input('Please input card_id manually: '))
                    break
                except ValueError:
                    print('Invalid input. Please enter an integer.')
            input_cache_dict[cache_key] = card_id  # 记录全局缓存
        return card_id


def check_order(exist_card_id, detail_id, expected_card_id):
    if exist_card_id == expected_card_id:
        print()


def update_order(detail_id, card_id):
    query = "UPDATE tb_order_detail SET card_id_id = %s WHERE ID = %s"
    query_db(query, (card_id, detail_id))


def insert_order(col_id, position, card_id):
    query = "INSERT into tb_order_detail (column_id_id, card_id_id, Order_Position) VALUES (%s, %s, %s)"
    insert_to_db(query, (col_id, card_id, position))


def check_insert_detail():
    season = 11
    for col_index, column in enumerate(s1_dict):
        column_id = get_column(season, col_index + 1)
        if not column_id:
            insert_column(season, col_index + 1)
            column_id = get_column(season, col_index + 1)
        for card_index, card in enumerate(column):
            display_index = len(column) - card_index  # display_order倒序
            print('----------check or insert begin for season {} column {} order {}----------'.format(season,
                                                                                                      col_index + 1,
                                                                                                      display_index))
            detail_res = get_exist_order(column_id, display_index)  # [0]: card_id, [1]: detail_id
            expected_card_id = fetch_card(season, display_index, col_index + 1, card['rank'], card['name'])
            if detail_res:
                if detail_res[0] == expected_card_id:
                    print('season {} column {} order {} check ok!'.format(season, col_index + 1, display_index))
                else:
                    exist_card_info = get_card_by_id(detail_res[0])
                    print('Find error Card in DB, id: {}, card_id: {}, name: {}, form: {}, exp_id: {}'.format(
                        detail_res[0],
                        exist_card_info[0],
                        exist_card_info[1],
                        exist_card_info[2],
                        expected_card_id))
                    while True:
                        ans = input('Do you want to correct the error? y/n')
                        if ans == 'y' or 'n':
                            break
                    if ans == 'y':
                        update_order(detail_res[1], expected_card_id)
                        print('Correct error ok! old_card: {}, new_card: {}'.format(exist_card_info[0],
                                                                                    expected_card_id))
            else:
                insert_order(column_id, display_index, expected_card_id)
            print('----------check or insert end----------')


def check_dict():
    new_dict = {}
    for col_index, column in enumerate(s1_dict):
        for card_index, card in enumerate(column):
            key = '{}_{}'.format(card['rank'], card['name'])
            if key in new_dict:
                new_dict[key] += 1
            else:
                new_dict[key] = 1
    sorted_items = sorted(list(new_dict.items()), key=lambda x: x[0])
    for k, v in sorted_items:
        print('{}:{}'.format(k, v))


if __name__ == "__main__":
    check_insert_detail()
    # check_dict()
